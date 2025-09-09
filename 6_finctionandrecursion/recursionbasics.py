#Recursion :- Function calling itself

def show(n):
    if(n==0):
        return "end"
    print(n,end = " ")
    show(n-1)

show(10)