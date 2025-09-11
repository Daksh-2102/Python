#searching 'learning' in the pratice.txt file

def searching():
    word = 'learning'
    with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")


searching()