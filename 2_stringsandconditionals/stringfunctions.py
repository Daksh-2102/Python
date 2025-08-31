#String functions 

str = "i am Daksh studying in 5th sem. i am 19 years old"

#1> str.endwiths(" ") :- It returns true if that substring exists in that string else false.
print(str.endswith("old")) # true
print(str.endswith("years")) #false 

#2> str.capitalize() :- It capitalizes the ist letter of the string.
print(str.capitalize())
print(str) # After one time it becomes the actual str.

#3> str.replace(old,new) :- It replaces all the occurences of old with new one.
print(str.replace("19","20"))

#4> str.find("word") :- It returns the index vallue  of that word of its ist occurence.
print(str.find("Daksh"))
print(str.find("i")) # It returns index value of ist occurence of "i".

#5> str.count("word") #Counts the occurence of that word
print(str.count("am"))