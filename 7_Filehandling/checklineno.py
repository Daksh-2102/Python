#Function to check the word is present or not

def check_learning():
    word = 'learning'
    with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'r') as f:
        data = f.read()
        if(word in data):
            print("yes")
        else:
            print("No")

check_learning()
#Func to check the line no.

def line_no():
    word = 'learning'
    data = 1
    line_num = 1

    with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_num)
                return
            line_num +=1
    return -1

line_no()            