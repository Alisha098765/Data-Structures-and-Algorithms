import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

num = int(input("Enter the number you want to search:"))

if num in array:
    print("Yes, the number is present in the array.")
else:
    print("No, the number is not present in the array.")


print(array[3])