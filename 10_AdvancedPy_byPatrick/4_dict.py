#Dict are the key value pairs that are mutable, unordered

dict1 = {
    'name' : 'daksh',
    'age' : 19,
    'rollno' : 3
}
print(type(dict1))
print((dict1))

#we can too create a dict using the dict fxn
dict2 = dict(name = 'daksh', age = 19 , city = 'Jmu')
print(type(dict2))

#Access particular dict item

print(dict1['name']), print(dict1['age'])

#addng elems

dict1['email'] = 'dakshvasu21@gmail.com'
print(dict1)


try:
    print("yes", dict1['lname'])
except :
    print("Error")

#for separetely printing keys or values

for keys in dict1.keys():
    print(keys)
    
print(dict1.values())