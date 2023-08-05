from collections import namedtuple

student = namedtuple('student', ['name' , 'age' , 'DOB'])

s = student('Alisha' , 12 , 2)

print(s[1])

print(s.age)