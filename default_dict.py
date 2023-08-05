from collections import defaultdict

dict = defaultdict(int)

a = [1 ,2 , 3 , 4 ,5 ,6 ,7]

for i in a:
    dict[i]+=1

print(dict)

