# -*- coding: utf-8 -*-
"""
Created on Sun May 12 15:24:12 2024

@author: tbbra
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# SCROLL TO BOTOM AND FILL OUT DT AND FILENAME


class TextReader:
    def __init__(self,filename):
        
        self.file = filename
        self.vals = []
        

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
    def finddt(self):
        # Find the delta t in seconds
        # Assuming the first column is time in seconds
        time_col = self.vals[0]

        minutes, seconds = time_col[0].split(':')
        total_seconds = int(minutes) * 60 + float(seconds)  

        minutes, seconds = time_col[1].split(':')
        next_total_seconds = int(minutes) * 60 + float(seconds)

        dt = next_total_seconds - total_seconds

        return dt  
        

    
    def summary_stats(self, column):
        # Calculate summary statistics for a given column
        # Convert the column to a numpy array for easier calculations
        column_data = np.array(self.vals[column], dtype=float)
        mean = np.mean(column_data)
        median = np.median(column_data)
        std_dev = np.std(column_data)
        min_val = np.min(column_data)
        max_val = np.max(column_data)
        return mean, median, std_dev, min_val, max_val
    
            
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
        
    def saveSubset():
        return 0
    

if __name__ == "__main__":
    # ACTION make your code her, there are lots of helpers in the class above
    # ACTION: what is the filename
    filename = r'C:\Users\tbbra\Documents\CNT research - vanfleet\Ozone testing\Try 3\d.txt'

    # ACTION what col do you want to graph, 0 based
    col = 1

    text = TextReader(filename)
    var = text.readstuff(filename)

    dt = text.finddt()

    # ACTION: start and end in seconds for both!
    start = 68000
    end = (len(var.vals[col]) - 1) * dt

    # ACTION: title for graph
    title = 'Pressure vs Time'
    text.makeGraphs(var.vals[col], start, end, "Time (Sec)", "Pressure (Torr)", title, dt)

