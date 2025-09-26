#we can open multiple files by using with statement


# Opening two files together using `with` and parentheses
with (
    open('/home/daksh/Documents/pythoncodes/9_AdvancePython/file1.txt', 'r') as f1,
    open('/home/daksh/Documents/pythoncodes/9_AdvancePython/file2.txt', 'r') as f2
):
    # Read contents of both files
    content1 = f1.read()
    content2 = f2.read()

print("File 1 content:")
print(content1)
print("\nFile 2 content:")
print(content2)
