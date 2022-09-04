i = int(input("Row: "))
j = int(input("Column: "))

matrix = [[0 for col in range(j)] for row in range(i)]

for row in range(i):
    for col in range(j):
        matrix[row][col] = row * col
print(matrix)
