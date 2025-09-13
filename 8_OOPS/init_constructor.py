# __init__ construuctor

class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("Add Students")

s1 = Student("Daksh")
print(s1.name)

s2 = Student("Vasu")
print(s2.name)