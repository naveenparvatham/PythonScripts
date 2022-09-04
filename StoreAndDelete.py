# Q(3): Storing “Age” and “PhD” columns in one DataFrame and delete the data
# of all people who don’t have a PhD
import numpy as np
import csv as cs
import pandas as pd

# emp_box = []
# with open('PHD_2.csv', 'rt') as f:
#     data2 = cs.reader(f)
#     for row in data2:
#         str1 = str(row)
#         if row[3] == "PHD":
#             emp_box.append((row[0], row[1]))
# print(pd.DataFrame(emp_box))

# Q(4): Calculate the total number of people who have a PhD degree from SalaryGender CSV file.

count = 0
with open('PHD_2.csv', 'rt') as f:
    data2 = cs.reader(f)
    for row in data2:
        str1 = str(row)
        if row[3] == "PHD":
            count += 1
print(count)
