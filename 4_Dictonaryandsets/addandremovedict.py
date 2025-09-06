# adding elements in Dict.

dict1 = {
    'name' : 'vasu',
    'age' : 19,
    'height' : 5.10,
    'eye_color' : 'brown'
}

#1. 
dict1["skin_color"] = "brwonish"
print(dict1)

#2.
dict1.update({'gmail' : 'dakshvasu21@gmail.com'})
print(dict1)

#removing the items

#1. .pop() :- unlike set, it pops the particular key -> value
(dict1.pop("eye_color"))
print(dict1) 

#2. item() :- will remove the last inserted item of the dict
dict1.popitem()
print(dict1)

#3. del is the keyword used to delete the particular value using key and can dlt the whole dict as well.