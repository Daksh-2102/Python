#self is the paramter which we passes as ist argument

class Car:
    brand = "Audi"
    color = "Black"

    def func(self):
        print(f"The cars is {self.brand} and color is {self.color} ")

car1 = Car()
car1.func()
