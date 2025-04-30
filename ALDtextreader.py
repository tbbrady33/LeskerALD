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
        

    def readstuff(self,filename):
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
        cols = wholething[0].count(',') + 1
        # print(cols)
        rows = len(wholething)
        # print(rows)
        #orgainzed array of arrays
        self.vals = [ [[] for i in range(rows)] for i in range(cols)]
        
        # Now organize into vals
        for i in range(rows):
            split_row = wholething[i].split(',')
            for j in range(cols):
                try:
                    self.vals[j][i] = split_row[j]
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
    
    def makeGraphs(self,data_series,start,end,xlabel,ylabel,title,dt):
        start = int(start/dt)
        end = int(end/dt)
        # Ensure data_series contains only numeric values
       
        
        data_series = [float(value) if str(value).replace('.', '', 1).isdigit() else None for value in data_series]
        data_series = [value for value in data_series if value is not None]

        #how big should T be
        # put the delta T in the cell below in seconds
        sliced_data = data_series[start:end]

         # Make time array that matches the data
        time = np.linspace(start*dt, end*dt, len(sliced_data))

        # Extra code to separate different things
        plt.figure()
        plt.plot(time, sliced_data)
        plt.ticklabel_format(style='plain', axis='x')

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.title(title)
        plt.show()
        return 0
        
#ACTION: what is the filename

filename = r'C:\Users\tbbra\Documents\CNT research - vanfleet\Ozone testing\Try 3\d.txt'

#ACTION: what is the dt 
dt = .1

#ACTION what col do you want to graph, 0 based

col = 1



text = textReader(filename)


var = text.readstuff(filename)

#ACTION: start and end in seconds for both!
start = 68000

end = (len(var.vals[col]) - 1) *dt

# thing = text.timeArray(var.vals[0], start, end)
# print(len(thing))
print(len(var.vals[col]))

#action: title for graph
title = 'Pressure vs Time'

text.makeGraphs(var.vals[col], start, end, "Time (Sec)", "Pressure(Torr)", title, dt)