num = int(input("Enter the number of elements you want to store in an array:"))

arr= []



print("Enter",num,"Elements")

for i in range(num):
    elements = int(input())
    arr.append(elements)

print("The array is:" , arr)

val = int(input("Enter the value you want to delete:"))

if val in arr:
    arr.remove(val)
    print("The updated array is: " , arr)

else:
    print("Element is not exist here ")



