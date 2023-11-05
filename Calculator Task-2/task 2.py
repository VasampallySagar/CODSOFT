def add():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The Addition of two numbers:",a+b)
def sub():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The Subtraction of two numbers:",a-b)
def mul():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The Multiplication of two numbers:",a*b)
def div():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The Division of two numbers:",a/b)
def modulo():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The modulo division of two numbers:",a%b)
def expo():
    a=int(input("enter the 1'st number:"))
    b=int(input("enter the 2'nd number:"))
    print("The Exponent:",a**b)

while True:
    print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Modulo Division 6.Exponent 7.Exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        modulo()
    elif choice==6:
        expo()
    elif choice==7:
        print("program exited!")
        break
    else:
        print("Enter a valid choice!")
   
    
    
