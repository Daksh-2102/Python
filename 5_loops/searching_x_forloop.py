#searching  x using for loop

tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter x :"))
index = 0

for i in tup:
    if(i==x):
        print(f"{x} found at ",index)
        break
    index+=1

else:
    print(f"{x} not found")