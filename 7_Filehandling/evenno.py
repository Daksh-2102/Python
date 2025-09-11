# print the count of even numbers from the evenno.txt file

count = 0

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/evenno.txt",'r') as f:
    data = f.read()

    new = data.split(",")

    for i in new:
        if(int(i) % 2 ==0):
            count+=1
print(count)