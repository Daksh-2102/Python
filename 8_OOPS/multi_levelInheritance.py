#multi-level inheritance

class Employee:

    name = "Daksh"
    company = "Google"

    def show(self):
        print(f"The name of the employee is {self.name} and his company is {self.company}")
        
#single inheritance
class Coder(Employee):
    language = "python"
    def show_again(self):
        print(f"{self.name} is {self.language} developer in {self.company}")

# multilevel inheritance :- cant use mro method + coder inherits both the properties of Employee and Coder  
class Cyber(Coder):
    cybersecuirty = "Penetration testing"
    def show_cyber(self):
        print(f"{self.name} who is a {self.language} developer is also an {self.cybersecuirty}")


emp1 = Employee() #This only print the language attr
emp1.show()

coder1 = Coder()
emp1.show()
coder1.show_again() #since it contains both it prints both except cyber one


cyber1 = Cyber() #it prints all attributes
cyber1.show()
cyber1.show_again()
cyber1.show_cyber()