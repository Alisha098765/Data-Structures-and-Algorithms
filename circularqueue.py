class CircularQueue():

    def __init__(self , size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.front = self.rear = -1

    def enqueue(self , data):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full" , end = " ")
        
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data

    
    def dequeue(self):

        if self.front == -1:
            print("Queue is empty" , end = " ")

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
        
    def display(self):

        if 

            

            

            



