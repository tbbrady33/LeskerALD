# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:24:12 2024

@author: tbbra
"""

import numpy as np
import matplotlib.pyplot as plt

#MAKE SURE TO: delete all the headers from the text file,
# this is the text file from the pressure not the elipsometry

file = open("C:\\Users\\tbbra\\OneDrive\\Documents\\CNT research - vanfleet\\Baseline\\20 cycles Alumna test.txt", "r")
content = file.read()

time = []
pressure = []
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


#now that everything is in a list we need to get the right information

for i in range(len( wholething)):
    if (i % 30 == 0):
        time.append(wholething[i])
    if (i % 30 == 2):
        pressure.append(float(wholething[i]))
        
#ACTION look ag the time array and see what the delta t is

dt = 1/9
L = dt* len(time)
N = len(time)
t = np.linspace(0,L,N)
        
#ploting now
plt.figure()
plt.plot(pressure)
#charnge your axis and label
plt.xlabel("time (seconds)")
plt.ylabel("Pressure (Torr)")
plt.title("Alummina basline pressures")