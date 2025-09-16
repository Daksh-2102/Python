#create a class programer for storing info of few programmer working at microsoft.

class Programmer:

    def __init__(self,name,salary,position):
        self.name = name
        self.salary = salary
        self.position = position

    def print_info(self):
        print(f"These programmers are working at Microsoft")

emp1 = Programmer("Daksh",2000000,"CyberExpert")
print(emp1.name,emp1.salary,emp1.position)

emp2 = Programmer("Pankaj","1000000","Full-Stack Developer")
print(emp2.name,emp2.salary,emp2.position)
