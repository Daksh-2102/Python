#Palindrome in the list

list = ["m","a","a","m"]
print(list)

list1 = list.copy()
list1.reverse()
print(list1)

if(list==list1):
    print("Yes its a palindrome")
else:
    print("not a palindrome")