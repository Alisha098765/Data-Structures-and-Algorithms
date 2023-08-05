from collections import UserDict

class MyDict(UserDict):

    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    

    def pop(self , s = None):
        raise RuntimeError("Deletion not allowed")
    
    def popitem(self , s = None):
        raise RuntimeError("Deletion not allowed")


d = MyDict({"name":"Alisha" , "age" : 21 , "Gender" : "Female"})

print(d)

d.pop("name")
    

    