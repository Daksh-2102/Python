#Instance vs Class Attributes
#we know that instance attr has more prefrences than class attr.

class Student:
    name = "Daksh"
    learns = "Py"

me = Student()
me.name = "Vasu" #it prints vasu as name because of the above reason.
print(me.name,me.learns)