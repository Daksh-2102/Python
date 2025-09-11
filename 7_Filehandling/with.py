#with syntax

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/with.txt","r") as f:
    data = f.read()
    print(data)

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/with.txt","w")as t:
    write_data = t.write("using with to overwrite the previous text\n")

with open("/home/daksh/Documents/pythoncodes/7_Filehandling/with.txt","a")as p:
    append_data = p.write("It will overwrite in the end\n")