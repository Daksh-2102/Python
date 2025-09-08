#table using func

def tables(n):
    i = 1
    while i <=10:
        print(f"{n} * {i} = {n*i}")
        i+=1

tables(17)

#2.

def table(m):
    for i in range(1,11):
        print(f"{m} * {i} = {m*i}")
        i+=1

table(2)
