#Semester gradings

Network_Security = int(input("Marks = "))
ODS =  int(input("Marks = "))
RT = int(input("Marks = "))
SE = int(input("Marks = "))

Percentage = (((Network_Security + ODS + RT + SE )/ 500) * 100)
print("Percentage in this semester = " ,round(Percentage,2))

#percentage to cgpa :- percentage = cgpa * 9.5
cgpa = Percentage/9.5

print("Cgpa in this semester = " ,round(cgpa,2))