#SIMPLE CALCULATOR

def Addition():
    Sum=0
    Number=int(input("Enter how many numbers needs to be added:"))
    for i in range (Number):
        User=int(input("Enter the numbers to be added:"))
        Sum+=User
    print("The final answer is:",Sum)

def Subtraction():
    Number1=int(input("Enter the first number:"))
    Number2=int(input("Enter the second number:"))
    Subtraction=Number1-Number2
    print("The final answer is:",Subtraction)

def Multiplication():
    Product=1
    Number=int(input("Enter how many numbers to be multiplied:"))
    for i in range (Number):
        User=int(input("Enter the numbers to be multiplied:"))
        Product*=User
    print("The final answer is:",Product)

def Division():
    try:
         Dividend=int(input("Enter the dividend:"))
         Divisor=int(input("Enter the divisor:"))
         Quotient=Dividend/Divisor
         print("The final answer is:",Quotient)
    except ZeroDivisionError:
        print("Divisor cannot be zero!")

ch="yes"
while ch.lower()in ["yes","y"]:
    print("---SIMPLE CALCULATOR---")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        Addition()
    elif choice==2:
        Subtraction()
    elif choice==3:
        Multiplication()
    elif choice==4:
        Division()
    elif choice==5:
        print("Thanks for using calculator!")
        break
    else:
        print("Invalid choice entered!")

    ch=input("Do you want to continue(yes/y):")
