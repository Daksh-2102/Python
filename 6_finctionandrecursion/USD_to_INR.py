#converting usd into inr

def converter(usd_amount):
    inr_value = usd_amount * 88.10
    print(usd_amount,"$","=",inr_value,"rs" )

usd_amount = int(input("Enter amount in usd : "))
converter(usd_amount)