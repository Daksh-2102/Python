#Dunder methods :- methods that starts from __ __ (underscore) are called dunder methods.

class Employee:

    def __init__(self,name,salary,lan):
        self.name = name
        self.salary = salary
        self.language = lan
    
    def use_func(self):
        print(f"The name of the employee is {self.name} and his salary is {self.salary} and his language is {self.language}")

emp1 = Employee("Daksh",100000,"python")
emp1.use_func()
