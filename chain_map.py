from collections import ChainMap

d1 = {'a' : 1 , 'b' : 2}
d2 = {'c' : 1 , 'd' : 2}
d3 = {'e' : 1 , 'f' : 2}
d4 = {'g' : 1 , 'h' : 2}

c = ChainMap(d1 , d2 , d3 , d4)
print(c)

print(c['a'])
