#strings part 2
from timeit import default_timer as T
str1 = ['a']* 100000
# print(str1) #['a', 'a', 'a', 'a', 'a', 'a']

#bad way
start = T()
string = "" 
for i in str1:
    string+=i
stop = T()
# print(string)
print(stop - start)


#good way

#join them :- if wants to join any str use join fxn
start = T()
# print("".join(str1)) #aaaaaa
stop = T()
print(stop - start)

 