#log system

def log_checking():

    try:
        with open("/home/daksh/Documents/pythoncodes/9_AdancePython/file1.txt",'r') as f:
            data = f.read()

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("permissions not granted")

    else:
        print(data)


log_checking()