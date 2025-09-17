#multiple inheritance

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

# multiple inheritance :- cant use mro method + coder inherits both the properties of Employee and Coder  
class Cyber(Coder):
    cybersecuirty = "Penetration testing"
    def show_cyber(self):
        print(f"{self.name} who is a {self.language} developer is also an {self.cybersecuirty}")


emp1 = Employee()
emp1.show()

coder1 = Coder()
coder1.show_again()

cyber1 = Cyber()
cyber1.show_cyber()