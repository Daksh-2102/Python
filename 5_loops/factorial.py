#factorail

n = int(input("Enter n :"))
fact = 1
for i in range(1,n+1):
    fact*=i

print(f"factorial of {n} = ",end = "")
print(fact)