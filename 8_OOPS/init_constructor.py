# __init__ construuctor

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Add Students")

s1 = Student("Daksh" , 100)
print(s1.name,s1.marks)

s2 = Student("Vasu", 99)
print(s2.name,s2.marks)