#Type defition -> defining the type of that variable

n : int  = 5 

name : str = "daksh"

if name.find('s'):
    print("Present hai")
else :
    print("Absent hai")


n = name.capitalize()
print(n)

#In func

def sum(a : int , b : int) -> int :
    sum = a+b
    print(sum)

a = int(input("Enter a :"))
b = int(input("Enter b :"))

sum(a,b)
 