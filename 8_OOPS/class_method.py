#class method :- Class method is used to print the class attr even if there is any changes in it.

class Employee:
    a = 54
    @classmethod
    def show(cls):
        print(f"My class attr is {cls.a}")

emp1 = Employee()
emp1.a = 22

emp1.show()