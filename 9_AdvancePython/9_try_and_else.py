#try except and else

''' if the "if" statements hits, it will print the statement and runs the else statement as well
but if statements fail it goes to else but , in case we done some error it runs value error '''


try:
    n = int(input("Enter n : "))
    if(n==6):
        print("Good")

except ValueError:
    print("Error found")


else:
    print("workdone , now i m in else block")