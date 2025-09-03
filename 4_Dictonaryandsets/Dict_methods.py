#Methods in Dictonries

student = {
    "name" : "vasu",
    "age" : 19,
    "marks" : {
        "maths" : 99,
        "phy" : 88
    }
}
#1. Dict.keys() :- It will return all the keys of the Dict
print(student.keys()) # dict_keys(['name', 'age', 'marks'])
print(list(student.keys())) #it will return keys in list ['name','age','marks']
print(len(student)) # length of keys

#2. Dict.values() :- It will return all the values of the Dict
print(student.values()) #dict_values(['vasu', 19, {'maths': 99, 'phy': 88}])
print(tuple(student.values())) #it will return keys in tuple .('vasu', 19, {'maths': 99, 'phy': 88})
print(len(student.values())) # length of values

#3. Dict.items() :- It return all the (key,value) pairs as tuples.
print(student.items()) #dict_items([('name', 'vasu'), ('age', 19), ('marks', {'maths': 99, 'phy': 88})])

#we can access these tuples value 
pairs = list(student.items())
print(pairs[1])

#4. Dict.get("") :- helps to get the value of that key
print(student.get("name"),student.get("age"))

#5. Dict.update() :- for updating our dict later on
student.update({"name" : "daksh","age" : 18 })
print(student)