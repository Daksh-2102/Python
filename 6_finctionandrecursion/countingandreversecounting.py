# counting and reverse counting

def counting(n):
    for i in range(1,11):
        print(i)

print("counting :",end = " ")
counting(10)
print("\n")

#reverse  counting

def reverse_counting():
    for i in range(10,0,-1):
        print(i,end=" ")
        i+=1

print("reverse counting : ",end = " ")
reverse_counting()