'''Create a class 'Pets' from a class 'Animals' and futher  create a 'Dog' from 'Pets' 
Add a method 'bark' to class 'Dog' '''

class Animals:
    def __init__(self):
        print(f"It's a animal")

class Pets(Animals):
    def __init__(self):
        print(f"I m taking a pet")

class Dogs(Pets):
    def __init__(self):
        print(f"The Pet is Dog")

    def bark(Dogs):
        print("My Pet Dog is barking on strangers")

# Ani = Animals()

# pet = Pets()

dog = Dogs()
print(dog.bark())