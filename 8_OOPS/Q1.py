'''creating a class Student and storing names and marks of 3 student in the constructor.
Then make a method and find the average '''

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("Name :",self.name,"and your","average :",round(sum/3,2))
      
    
s1 = Student("Daksh",[80,90,100])
s1.average()

s2 = Student("vasu",[12,89,90])
s2.average()


s3 = Student("vasu",[78,85,60])
s3.average()