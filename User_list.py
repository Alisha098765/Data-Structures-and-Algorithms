from collections import UserList

class MyList(UserList):

    def remove(self , s = None):
       raise RuntimeError("Not Possible")
    

    def append(self , s = None):
        raise RuntimeError("Not Possible")
    
    def pop(self , s = None):
        raise RuntimeError("Not Possible")
    
L = MyList([1 , 2 , 3 , 4 ,5 ,6 , 7 ])

print(L)

L.pop(3)