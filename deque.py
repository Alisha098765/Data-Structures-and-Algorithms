import collections

de = collections.deque([1 , 2 , 3 , 4])

de.append(5)
print(de)

de.pop()
print(de)

de.popleft()
print(de)