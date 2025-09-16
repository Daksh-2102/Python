#create a calculator to find the square cube and square root of the number

class Calculator:

    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is : {self.n * self.n}")

    def cube(self):
        print(f"The cube of {self.n} is : {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root of {self.n} is : {self.n**0.5} ")

cal = Calculator(int(input("Enter n : ")))

cal.square()
cal.cube()
cal.square_root()