
import csv
import numpy as np
import matplotlib.pyplot as plt


#put the file name below make sure to change
vals = []
with open("off off pressure.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #what column is your data in - 1
        col = 1
        vals.append(float(row[col]))
        
# put the delta T in the cell below in seconds
dt = .1
time = np.arange(0,dt*len(vals),dt)
# extra code to seperate different things
# plt.figure()
# plt.plot(time,vals)
# plt.xlabel('Time (minutes)')
# plt.ylabel('Pressure (Torr)')
# plt.grid()
# plt.title("Pressure at 200 C with pump on and IGF flow")

# plt.figure()
# plt.plot(time[6000:500000],vals[6000:500000])
# plt.xlabel('Time (minutes)')
# plt.ylabel('Pressure (Torr)')
# plt.grid()
# plt.title("Pressure at 200 C with pump on and IGF flow")


#assuming completly linear leak rate
#line



plt.plot(time,vals)
# plt.xlabel('Time (minutes)')
# plt.ylabel('Pressure (Torr)')
# plt.title('Ploting with linear fit to end points with slope =' + str(slope))


plt.show()