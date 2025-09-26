#bank system using try except else and finally


def transactions(amount,balance):
    try:
        amount = int(amount)
        if amount > balance:
            raise ValueError("Insufficient balance")
        
    except ValueError as e: 
            print(f"Transaction failed",e)
    
    else:
        balance -=amount
        print(f"Withrawal done , current balance : {balance}")

    finally:
        print("Transaction closed")


balance = 1000
amount = int(input("Enter amount u want to withrawal : "))

transactions(amount,balance)


