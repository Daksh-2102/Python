#Sum of n numvbers using function

def sum_of_n_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

n = int(input("Enter n :"))
sum_of_n = sum_of_n_numbers(n)

print(f"sum from 1 to {n} :",sum_of_n)


#2.while 

def sum(m):
    sum = 0
    i = 1

    while i <= m:
        sum+=i
        i+=1
    return sum

m = int(input("Enter n :"))
sum1 = sum(m)
print(sum1) 