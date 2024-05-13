# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:05:11 2024

@author: tbbra
"""


import numpy as np
import matplotlib.pyplot as plt

#SCROLL TO BOTOM AND FILL OUT ACTIONS

class eipseStuff:
    def __init__(self,filename):
        self.filename = filename
        
    def readStuff(self,filename, cols):
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
                
                if(char.isspace()):
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
    
    def makeGraphs(self,timearray, array,start,end,xlabel,ylabel,title):
        
        
        #how big should T be
        
        #extra code to seperate different things
        plt.figure()
        plt.plot(timearray,array[start:end])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.title(title)
        
#ACTION: What is the filename in the current directory

filename = "BDMADMSTest3Tauc-Lorentzmodelidk.txt"

#ACTION: Number of columns in the file

cols = 3

#ACTION: what col do you want to graph 0 based

col = 1

#ACTION: what title do you want to add

title = "Thickness"


text = eipseStuff(filename)

var = text.readStuff(filename, cols)

num = len(var.vals[0]) - 1

#ACTION: What is the first and last indexes that you would like to grpah

start = 5

end = num
text.makeGraphs(var.vals[0][start: end - start], var.vals[col][start:end], start, end, "Time", var.vals[col][0], title)



