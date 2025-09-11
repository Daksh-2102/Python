#File handling 
#we have to give the complete file path.
#always open the file, before performing any func.

f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/demo.txt","r")

# data = f.read()

# print(data) #reads all the data present there

line1 = f.readline() # reads line1
print(line1)

line2 = f.readline() #reads line2
print(line2)

# print(type(data))
f.close()