#Sum of ist n natural numbers using while loop

n = int(input("Enter n : "))

sum = 0

i = 1
print(f"Sum from {i} to {n} :",end=" ")

while i <= n:
    sum+=i
    i+=1

print(sum)
print("\nend\n")


#2. using range func
summ = 0
m = int(input("Enter m : "))
for j in range(1,m+1):
    summ+=j

print(summ)