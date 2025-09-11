# using some read write and append in my .txt file

f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/readandwrite.txt",'r')

data = f.read() #it will read through my readandwrite.txt
print(data) #will print the whole data

#now overwriting some text in my .txt file using 'w'

f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/readandwrite.txt",'w')
data = f.write("overwriting in the .txt file using w.\n")
print(data)

'''what happens is , after using 'w' i.e overwriting command, it dlts the previous text from
.txt file, and overwrites the new data  '''

f.close()

#for adding the new data with the previous data use 'a'
#append mode

f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/readandwrite.txt",'a')

f.write("includes the append ")

