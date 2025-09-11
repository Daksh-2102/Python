
#r+ : read and write in the start with the previous text.
f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/combiningmode.txt",'r+')
f.write("new text \n")

#w+ :- tranculates the file i.e deletes the above data 
f = open("/home/daksh/Documents/pythoncodes/7_Filehandling/combiningmode.txt",'w+')
f.write("It will delete the previous text and writes the new text")
