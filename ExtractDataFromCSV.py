# Q(1): given SalaryGender CSV file and store the data from each column in a separate NumPy array
import numpy as np
import csv as cs

lst = []
with open('SalaryGender.csv', 'rt') as f:
    data = cs.reader(f)
    for row in data:
        str1 = str(row)
        lst.append(str1)

for i in lst:
    x = i.split(',')
    y0 = np.array(x[0])
    y1 = np.array(x[1])
    y2 = np.array(x[2])
    print(y0, y1, y2)
