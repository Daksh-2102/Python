#Method

#creating class
class Student:

    def __init__(self,name):
        self.name = name
    
    #method creation
    def hello(self):
        print("hi",self.name)

s1 = Student("Vasuuu")
s1.hello()