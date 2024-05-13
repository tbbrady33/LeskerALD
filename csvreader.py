"""
Created on Sun May  12 15:24:12 2024

@author: Tyler Brady
"""


import csv
import numpy as np
import matplotlib.pyplot as plt
# SCROLL TO BOTOM AND FILL OUT DT AND FILENAME

class csvstuff:
    def __init__(self,dt,filename):
        # what is the dt
        self.dt = dt
        
        #what is the filename
        self.filename = filename
    
    
    def numRows(self,filename):
        largest = 0
        with open(filename, newline = '') as csvfile:
            spamreader = csv.reader(csvfile,delimiter = ',',quotechar = '/' )

            for row in spamreader:
                if (spamreader.line_num > largest):
                    largest = spamreader.line_num
        return largest
    
    #put the file name below make sure to change
    def readstufff(self,filename,num):
        self.vals = []
        self.head = []
        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            #heaaders
            lenth = False
            rows = -1
            for row in spamreader:
                rows += 1
                numofcols = num
                cols = -1
                for col in row:
                    cols += 1
                    numofrows = len(row)
                    if (lenth == False):
                        self.vals = [ [[] for i in range(numofcols)] for i in range(numofrows) ]
                        lenth = True
                    #headers
                    try:
                        integerthing = float(row[int(cols)])
                    
                    except ValueError:
                        try:
                            my_set = set(row[int(cols)])
                            if(':' in my_set):
                                self.vals[cols][rows] = row[int(cols)]
                                continue
                        except ValueError:
                            continue
                        else:
                            self.head.append((row[int(cols)]))
                            continue
                        
                    
                    self.vals[cols][rows] = (float(row[int(cols)]))
        return self
    
    def average(self, array, start, end):
        sum = 0
        for indexs in array[start:end]:
            sum += indexs
        
        return sum/len(array[start:end])
            
    def makeGraphs(self,array,start,end,xlabel,ylabel,title,dt):
        
        
        #how big should T be
        ending = dt*(end)
        # put the delta T in the cell below in seconds
        time = np.arange(start *dt,ending,dt)
        #extra code to seperate different things
        plt.figure()
        plt.plot(time,array[start:end])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.title(title)
    
#what is dt 
dt = 1

#ACTION: What is the filename in the current directory
filename = "Recording Set 2024.05.09-15.51.50 (1).csv"

csvs = csvstuff(dt,filename)

num = csvs.numRows(filename)

var = csvs.readstufff(filename,num)
#ACTION
#now what graphs do you want to make? (the number of rows is printed to the right)
#what col?
column = 2


csvs.makeGraphs(var.vals[column], 10, num-100, "time", "Concentration (%)", "Trial 1", csvs.dt) #ACTION put the labels titles and start row
# you can make more than graph in the same format as above

#average stuff if you want
av = csvs.average(var.vals[column], 10, num-100)
print("The average is: {average:.2f}".format(average = av))