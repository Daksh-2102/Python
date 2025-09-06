# searching x in the tuple

tup = (1,4,9,16,25,26,49,64,81,100)
# print(type(tup))

# x = int(input("enter x : "))
# if x in tup:
#     print(f"{x} is present in the tuple",)
# else:
#     print(f"{x} is not present in the tuple")

#2. using while loops

x = int(input("Enter x  : "))

i = 0
while i < len(tup):
    if(tup[i] == x):
        print(f"{x} is prsent in the tuple ")
        break
    i+=1
else:
    print(f"{x}is not present in the tuple")

print("End")