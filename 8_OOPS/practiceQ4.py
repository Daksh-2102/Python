'''create a class with class attr a ; create a object from it and set a directly using object.a = 0
Does it chnage the class attr'''

class Check:

    a = 4

bro = Check()
print(bro.a) #here the class attr is printed because there is no instance attr
bro.a = 0
print(bro.a)#here the instance attr is  created so printed instance attr, but no changes in class attr

print(Check.a)

'''here the answer for the above ques is no, because there are no changes in the class attr, jzt we r 
creating another instance attr'''