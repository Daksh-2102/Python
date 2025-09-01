#lists in python

marks = [100,79.9,0.89,88,111]

print(marks)
print(type(marks))
print(len(marks))

age = 18
name = input("Enter name : ")
address = str(input("Enter area :"))
marks = int(input("Enter marks : "))

student = (age,name,address,marks)
print(age,name,address,marks)
age = 19 # this shows that lists are mutable i.e lists can be modified but arrays cannot be modified i.e they r immutable
print(age,name,address,marks)

