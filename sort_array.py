array = [89 , 34 , 56 , 23 , 78 , 12 ]
temp = 0

print("original array is:")
for i in range(0 , len(array)):
    print(array[i] , end = " ")

print("sorted array")

for i in range(0 , len(array)):
    for j in range(i+1 , len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

#print()

for i in range(0 , len(array)):
    print(array[i])
