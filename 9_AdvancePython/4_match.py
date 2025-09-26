#match case :- similar as switch case in other languages

def network_protocols(protocol):
    match protocol:

        case 'http':
            print(f"{protocol} : HYPER TEXT TRANFER PROTOCOL")
        case 'https':
            print(f"{protocol} : HYPER TEXT TRANFER PROTOCOL SECURE")
        case 'ftp':
            print(f"{protocol} : FILE TRANFER PROTOCOL")
        case 'tls':
            print(f"{protocol} : TRANSPORT LAYER PROTOCOL")    
        case _:
            print(f"{protocol} : I don't want to add this protocol !! meri mrziiii :) ")


pro = input("Enter protocol : ")

network_protocols(pro)
        


