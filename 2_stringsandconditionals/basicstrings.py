# basics strings
str1 = "This is Daksh.\ni m in 5th sem.\n"
# print(str1)

# Concatenation
str2 = "my roll no. is 3"

print(str1+str2)

#length of string
print(len(str1))
print(len(str2))

#Indexing
str3 = "Daksh"
str3[0]
str3[1]
str3[2]
str3[3]
str3[4]

print(str3[0],str3[1],str3[2],str3[3],str3[4])

#Slicing  :- Accessing parts of the string and it doesn't includes last index value i.e 0 to n-1

str = "Dakshvasu"

print(str[0:4])
print(str[:7]) # it seems as str[0:7]
print(str[1:]) # it seems as str[1:str(len)]

#negative indexing 

neg = "apple"
print(neg[0:4])
print(neg[-3:-1])
print(neg[-5:len(neg)])