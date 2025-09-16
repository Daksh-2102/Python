#self is the paramter which we passes as ist argument

class Car:
    brand = "Audi"
    color = "Black"

    def func(self):
        print(f"The cars is {self.brand} and color is {self.color} ")

#if we don't want to pass the full object i.e self we jzt need to make that method a static method
    @staticmethod
    def wlcm():
        print("Wlcm to the showroom")
car1 = Car()
car1.func()
car1.wlcm()
