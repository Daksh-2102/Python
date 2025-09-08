#factorial of n number

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    return fact

n = int(input("Enter n : "))
factorial = fact(n)

print(f"factorial of {n} :",factorial)