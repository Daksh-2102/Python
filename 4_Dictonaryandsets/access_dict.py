#Accessing dict values in multiple ways.

student = {
    "name1" : "vasu",
    "name2" : "daksh",
    "roll" :   3,
    "marks" : 55.88
}

print("Original Dictinary items :\n",student)

#1.Dict("key")
print("marks of student = ",student["marks"])

#2. dict.get("key")
print(student.get("name2"))

#3. dict.keys() :- returns all the keys of the dict.
print(student.keys())

#4. dict.values() :- returns all the values of the dict.
print(student.values())