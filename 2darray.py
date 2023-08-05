row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))

two_d_array = [[0 for c in range(column)] for r in range(row)]

for r in range(row):
    for c in range(column):
        two_d_array[r][c] = r*c

print(two_d_array)