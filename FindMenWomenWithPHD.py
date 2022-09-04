# Q(2): Find: 1.The number of men with a PhD 2. The number of women with a PhD

import numpy as np
import csv as cs

with open('PHD.csv', 'rt') as f:
    data = cs.reader(f)
    for row in data:
        str1 = str(row)
        if row[3] == "PHD" and row[1] == "M":
            print(str1)

with open('PHD.csv', 'rt') as f:
    data1 = cs.reader(f)
    for row1 in data1:
        str2 = str(row1)
        if row1[3] == "PHD" and row1[1] == "F":
            print(row1)
