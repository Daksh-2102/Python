#basics of Dictonary
#Dictonary are used to stores data values in key : value pairs 
#we can stores any data type value and even we can store lists or tuples in it.
dict = {
    "name" : "Daksh",
    "subjects" : ["NS","ODS","Red Teaming"], #list
    "learning" : ("Cybersecuirty","python"), #tuples
    "roll_no." : 3,
    "marks" : 44.9
}
print(dict)

print(dict["name"],dict["subjects"])

#modification is possible in dict
dict["name"] = "vasu" 

# we can also add some other values in it.
dict["age"] = 19

print(dict)

null_dict = {} #we can create empty dictonary also
