#tables using while loops

i = 1
n = int(input("Enter n : "))

print("Table of", n, ":")
while i <= 10:
    print(n, "*", i, "=", n*i)
    i+=1

print("End\n\n")

#2. usinfg f string

j = 1
m = int(input("Enter m :"))

print(f"table of {m}",":")


while j <= 10:
    print(f"{m} * {j} = {m*j}")
    j+=1
