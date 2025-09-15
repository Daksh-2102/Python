#basics oops

class Employee:

    language = "Python"
    salary = 1000000

me = Employee()
me.name = "Daksh"
print(me.name,me.language,me.salary)

friend = Employee()
friend.name = "Pankaj"
print(friend.name,friend.language,friend.salary)

#here language and salary are class attributes whereas, name is instance/object attruibute.
