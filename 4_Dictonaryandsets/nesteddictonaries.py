#nesting in Dictonary

student = {
    "name" : "Daksh",
    "marks" : {       #nesting
        "maths" : 90,
        "phy" : 80,
        "chem" : 88,
    }
}

print(student) # It will print whole dict

print(student["marks"]) #It will seperately print the marks dict

#To print the nested part of the dict
print(student["marks"]["maths"])