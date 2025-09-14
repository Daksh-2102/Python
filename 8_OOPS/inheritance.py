#Inheritance :- when one class(child) derives the properties/methods of parent class

class Car:
    @staticmethod
    def start():
        print("Car starts...")

    @staticmethod
    def stop():
        print("Car stops...")

class Audicar(Car):
    def __init__(self,color):
        self.color = color

car1 = Audicar("Brown")
print(car1.start())

print(car1.stop())

