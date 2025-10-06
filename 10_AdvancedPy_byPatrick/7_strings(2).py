#strings part 2
from timeit import default_timer as T
str1 = ['a']*6
print(str1) #['a', 'a', 'a', 'a', 'a', 'a']

#bad way
# start = T()
string = "" 
for i in str1:
    string+=i
print(string)


#good wa6y

#join them :- if wants to join any str use join fxn
print("".join(str1)) #aaaaaa


