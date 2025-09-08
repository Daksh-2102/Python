#Average of 3 numbers 

def average_func(a,b,c):
    average  = (a+b+c)/3
    return average

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

print(f"Average of {a} , {b} , {c} : ",end = " ")
averagee = average_func(a,b,c)
print(round(averagee,2))
