Set = set([1 , 2 , 3 , 3 ,6,7, 'ALISHA' , 6 , 7 , 'For'])
print(Set)
print(type(Set))

for i in Set:
    print(i , end='')

print('ALISHA' in Set)

Set.add('Seerat')
print(Set)