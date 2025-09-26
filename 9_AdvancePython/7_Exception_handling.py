#exception : we can use try and except for smooth running of code even if there is any error in it.
'''like while making web page if web page doesn't loads it shows error as Page not loaded
i.e an eg of try and except'''


try:
    with open("/home/daksh/Documents/pythoncodes/9_AdvancePython/fle1.txt",'r') as f:
        data = f.read()
        print(data)

except FileNotFoundError :
    print("File1 not Found open file2")
    with open("/home/daksh/Documents/pythoncodes/9_AdvancePython/file2.txt",'r') as f:
        data = f.read()
        print(data)