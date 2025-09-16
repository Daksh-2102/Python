#Jzt adding a static methodtp greet 
class Calculator:

    def __init__(self,n):
        self.n = n
    @staticmethod
    def greet():
        print("hello")
    
    def square(self):
        print(f"The square of {self.n} is : {self.n * self.n}")

    def cube(self):
        print(f"The cube of {self.n} is : {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root of {self.n} is : {self.n**0.5} ")

cal = Calculator(int(input("Enter n : ")))
cal.greet()
cal.square()
cal.cube()
cal.square_root()