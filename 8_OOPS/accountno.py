#bank details 

class Account:

    def __init__(self,acc,bal):
        self.account = acc
        self.balance = bal

    def credit(self,amount):
        self.balance +=amount
        print("Rs",self.balance,"is credited in your account -->",self.account)
        print("balance -->",self.balance)

    def debit(self,amount):
      if amount > self.balance:
          print("Insufficient balance ")
      else:
        self.balance -=amount
        print("Rs",self.balance,"is debited from your account -->",self.account)
        print("balance -->",self.balance)

    def check_balance(self):
        print("Balance -->",self.balance)


#user input

acc1 = Account(8816,1000)

def account_updation():
    credits = int(input("Enter 1 for credit\nEnter 2 for debit\nEnter 3 for checking the balance :\n"))

    match(credits):
        case 1:
            amount = int(input("Enter your amount to credit: "))
            acc1.credit(amount)
        case 2:
            amount = int(input("Enter your amount to debit: "))
            acc1.debit(amount)
        case 3:
            acc1.check_balance()
        case _:
            print("Invalid choice")
account_updation()
