'''creating a "pratice.txt" file using python and add the data'''

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'w') as f:
    data = f.write("Hi everyone\nwe are learning file I/O\nusing Java\nI like programming in Java")

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'r') as f:
    data = f.read()
    print(data)


new_data = data.replace("Java","Python")

print("\nAfter changes\n")
print(new_data)

#now overwrite using the above to makechanges in the .txt file

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/pratice.txt",'w') as f:
    f.write(new_data)