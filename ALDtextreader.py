# -*- coding: utf-8 -*-
"""
Created on Sun May 12 15:24:12 2024

@author: tbbra
"""

import numpy as np
import matplotlib.pyplot as plt

# SCROLL TO BOTOM AND FILL OUT DT AND FILENAME


class textReader:
    import numpy as np
    import matplotlib.pyplot as plt
    def __init__(self,filename):
        
        self.file = filename
        

    def readstuff(self,filename, cols):
        self.vals = []
        file = open(filename, "r")
        content = file.read()
        #lets get the right number of rows and cols
        wholething = []

        curindex = 0
        imagindex = 0
        try:
            while (True):
                if (imagindex >= len(content)):
                    break
                char = content[imagindex]
                
                if(char == '\n' or char == '\t'):
                    endindex = imagindex
                    wholething.append(content[curindex:endindex])
                    curindex = endindex + 1
                imagindex += 1
        except EOFError or IndexError:
            pass
        file.close()
        
        rows = round(len(wholething)/cols)
        #orgainzed array of arrays
        self.vals = [ [[] for i in range(rows)] for i in range(cols)]
        
        #now organize into vals
        try: 
            for i in range(rows):
                for j in range(cols):
                    try:
                        self.vals[j][i] = float(wholething[i*cols + j])
                    except ValueError:
                        self.vals[j][i] = wholething[i*cols + j]
        except IndexError:
            pass
        
        return self
    def timeArray(self,array, start,end):
        for i in range(end - start):
            array[i + start] = array[i+start][:-3]
        
        newtime = []
        starthour = array[start][:2]
        startmin = array[start][3:5]
        startsec = array[start][6:]
        curhour = starthour
        skipcount = 0
        for i in range(end - start):
            if curhour == array[i+ start][:2]:
                if startmin == array[i+start][3:5]:
                    if len(newtime)== 0:
                        curtimesec = float(array[i + start][6:])
                        newtime.append(curtimesec + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)))
                    else:
                        curtimesec = float(array[i + start][6:]) - newtime[-1] + self.hourtosec(float(starthour)) + self.mintosec(float(startmin))
                        newtime.append(curtimesec + newtime[-1])
                else:
                    startmin = array[i+start][3:5]
                    curtimesec = float(array[i + start][6:]) + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)) - newtime[-1]
                    newtime.append(curtimesec + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)))
                    
            else:
                starthour = array[i+start][:2]
                if startmin == array[i+start][3:5]:
                    if len(newtime)== 0:
                        curtimesec = float(array[i + start][6:])
                        newtime.append(curtimesec + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)))
                    else:
                        curtimesec = float(array[i + start][6:]) - newtime[-1] + self.hourtosec(float(starthour)) + self.mintosec(float(startmin))
                        newtime.append(curtimesec + newtime[-1])
                else:
                    startmin = array[i+start][3:5]
                    curtimesec = float(array[i + start][6:]) + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)) - newtime[-1]
                    newtime.append(curtimesec + self.hourtosec(float(starthour)) + self.mintosec(float(startmin)))
                    
    def hourtosec(self,hour):
        return hour*3600
 
    def mintosec(self, minute):
        return minute*60
    
    def makeGraphs(self,array,start,end,xlabel,ylabel,title,dt):
        
        
        #how big should T be
        ending = round(dt*(end))
        # put the delta T in the cell below in seconds
        time = np.linspace(start*dt,ending,end)

        #extra code to seperate different things
        plt.figure()
        plt.plot(time[start:end],array[start:end])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.title(title)
        
#ACTION: what is the filename

filename = "presure, depo.txt"

#ACTION: what is the dt 
dt = .1

#ACTION what is the start and end, the end is 6000
start = 10
end = 6000

#ACTION how many cols are there (should be 20)

cols = 20

#ACTION what col do you want to graph, 0 based

col = 1



text = textReader(filename)


var = text.readstuff(filename, cols)
thing = text.timeArray(var.vals[0], start, end)

text.makeGraphs(var.vals[col], start, end, "Time (Sec)", "Pressure(Torr)", "Last couple of cycles", dt)