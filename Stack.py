#implementation using List:

stack = [2 , 3 , 4 ,5 , 6 , 7]

stack.append(10)
print(stack)

stack.pop()
print(stack)

#implementation using deque:

from collections import deque


d = deque([2, 3 ,4 , 5 , 7 , 8])

d.append(13)
print(d)

d.pop()
print(d)


############from queue module##########

from queue import LifoQueue

stack = LifoQueue(maxsize=3)

stack.put(2)
stack.put(2)
stack.put(2)
for item in stack.queue:
    print(item)
print(stack.qsize())
print(stack.full())




