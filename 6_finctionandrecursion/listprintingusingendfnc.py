#list printing using end func

def list_printing(list):
    for i in list:
        print(i,end = " ")

persons_rollno = ('vasu',3,'bansh',6,'vivek',41,'raghu',20)
list_printing(persons_rollno)