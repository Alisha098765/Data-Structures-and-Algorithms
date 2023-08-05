from collections import OrderedDict

print("Orginal List")

od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key , value in od.items() :
    print(key , value)


od.pop('c')

for key, value in od.items():
    print(key,value)


    






