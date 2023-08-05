from collections import UserString

class Mystring(UserString):

    def append(self , s):
        self.data += s

    def remove(self , s):
        self.data = self.data.replace(s , '')


s1 = Mystring("Geeks")

#s1.append("s")

#print(s1)

s1.remove("s")
print(s1)