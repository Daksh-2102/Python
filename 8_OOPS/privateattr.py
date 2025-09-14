''' Priavate attributes are those attributes that are only accessable inside the class
and not accessable outside the class'''

class Person:

    #we can create pvt attr using double underscore(__)
    def __init__(self,name):
        self.name = name
    def __heloo(self):
        print("Helooo gg")

    def wlcm(self):
        self.__heloo()

p1 = Person("Daksh")
# print(p1.name)

# p1.__heloo()
p1.wlcm()


