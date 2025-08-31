# Conditional Statements -> Grades

grades = int(input("marks = "))

if(grades >=90 and grades <=100):
    print("A")
elif(grades >=80 and grades <90):
    print("B")
elif(grades >=70 and grades <80):
    print("C")
elif(grades >=60 and grades <70):
    print("D")
elif(grades >=50 and grades <60):
    print("E")
else:
    print("fail")
