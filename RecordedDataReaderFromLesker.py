# -*- coding: utf-8 -*-
"""
Just trying to decifer the CSV that I was given for the Ozone.

"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys
from pathlib import Path



# TODO: Put the file name here!!!!
# Make sure you are in the correct directory
#ALSO: delete everything above the headers
filename = Path(
    r'C:\Users\tbbra\Documents',
    'CNT research - vanfleet',
    'Ozone testing',
    'Try 3',
    'd.csv'
)


def main():
    vals, head, start = openFileReturnLists(filename)
    numcols = len(head)
    print('There are {} headers in that file, which would you like to see? Just type the number'.format(numcols))
    
    num = 0
    for name in head:
        num+= 1
        print('{}: {}'.format(num, name))
    
    
    while True:
        choice = input(": ")
        if choice.isdigit():  # Checks if input is all digits
            choice = int(choice)  # Convert to integer
            break  # Exit the loop if it's valid
        else:
            print("Invalid input. Please enter an integer.")
    
    transpose = vals.T
    
    #get time array
    numrows= len(transpose[0])
    time = []
    for i in range(numrows):
        t = timeFromStart(start, transpose[0][i])
        time.append(t)
    print('Give me a name for the graph: ')
    name = input(': ')
    graph(name, time, transpose[choice - 1], head[choice - 1])
    return 0

def graph(name, time, data_series, label):
    # Ensure data_series contains only numeric values
    data_series = [float(value) if str(value).replace('.', '', 1).isdigit() else None for value in data_series]
    data_series = [value for value in data_series if value is not None]
    plt.plot(time[:len(data_series)], data_series)  # Plot the filtered data

    # Labels and title
    plt.xlabel("Time")
    plt.ylabel(label)
    plt.title(name)

    # Limit the number of y-axis ticks for readability
    plt.locator_params(axis='y', nbins=10)

    # Show the graph
    plt.grid(True, linestyle='--', alpha=0.6)  # Light dashed grid for clarity
    plt.show()
    return

def openFileReturnLists(filename):
    vals = []  # Will collect rows as lists
    head = []
    start = None

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row_idx, row in enumerate(reader):
            if row_idx == 0:
                head = row  # Save the header
            elif row_idx == 1:
                start = row[0]  # Save the starting timestamp
                vals.append(row)  # Also save the first data row
            else:
                vals.append(row)  # Save all other data rows

    vals = np.array(vals, dtype=object)  # Convert once at the end
    return vals, head, start

def timeFromStart(start,timestamp):
     dt = datetime.strptime(timestamp, "%b-%d-%Y %I:%M:%S.%f %p")
     dt2 = datetime.strptime(start,"%b-%d-%Y %I:%M:%S.%f %p")
     difference = dt - dt2
     sec = difference.total_seconds()
     return sec

if __name__ == '__main__':
    main()

