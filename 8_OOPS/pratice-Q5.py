'''Write a class Train which has methods to book the train ,get status(no. of seats) 
and get fare info about train is running Indain Railways'''

import random
class Train:

    def book(self,name,where,to,seat_reserved):
        self.name = name
        # self.ticketno = ticket_no
        self.where = where
        self.to = to
        self.seat_reserved = seat_reserved
        print(f"The deatils are : \n{self.name}\n{self.where}\n{self.to}\n{self.seat_reserved}\n")

    def get_status(self):
        print(f"The seat of {self.name} whose ticketno. is {random.randint(222,7777)} going from {self.where} to {self.to} has {self.seat_reserved} reserved seats")

    def fare(self):
        print(f"The above train is of Indain railways")

person1 = Train()
person1.book("Daksh","jammu","delhi",2)
person1.get_status()
person1.fare()