class Queue:

    def __init__(self):
        self.queue = []

    def Enqueue(self, item):
        self.queue.append(item)
        return item
    
    def Dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

q = Queue()

print(q.Enqueue(2))
print(q.Enqueue(4))
print(q.Enqueue(8))
print(q.Enqueue(12))

print(q.Dequeue())

print(q.display())
