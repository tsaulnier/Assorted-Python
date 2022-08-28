#/usr/bin/python3

# Note that the data file you need to use is in the ..\data folder:
#     "..\\data\\Tokyo-2020-Medals.csv"

#I spent 2 hours debugging this on problem 1. Côte d'Ivoire was saved as C?te d'Ivoire in the csv file
#and I was getting lots of esoteric errors with stack overflow recommending I install pandas to circumvent.
import csv
import sys

filename = 'data/Tokyo-2020-Medals.csv'
list = []
try:
    with open(filename, 'r', newline='\n') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            list.append(row)
except OSError:
    print("Could not open file:", filename)
    sys.exit()

size = len(list)
#descending bubble sort
while 1:
    p1 = 0
    p2 = 1
    switched = False
    while p2 < size:
        if int(list[p2][3]) > int(list[p1][3]):
            temp     = list[p1]
            list[p1] = list[p2]
            list[p2] = temp
            switched = True
        p1 += 1
        p2 += 1
    if not switched: break

# Print the output
reducedList = []
for element in list:
    reducedList.append([element[1], element[3]])

for i in range(len(reducedList)):
    print ('%-40s%-40s' % (reducedList[i][0], reducedList[i][1]))
