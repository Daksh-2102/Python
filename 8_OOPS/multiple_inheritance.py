#multiple inheritance :- inherits more than one class

class You:
    name = "Daksh"

class Her:
    she = ":("

class If_us(You,Her):
    we = "Daksh :)"

uss = If_us()

print(uss.name,uss.she,uss.we)