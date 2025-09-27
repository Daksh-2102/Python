#global variable

'''Golbal keyword will conisder the local var as global var and it print the global var as output'''
a = 3

def func():
    global a
    a = 333
    print(a)

func()
print(a)