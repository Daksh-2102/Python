#Add marks of 3 subjects in dict one by one in an empty dict

subjects = {}
print(type(subjects))

x = int(input("Enter phy marks = "))
subjects.update({"phy marks " : x})

y = int(input("Enter maths marks = "))
subjects.update({"maths marks " : y})

z = int(input("Enter chem marks = "))
subjects.update({"chem marks ": z})

print(subjects)