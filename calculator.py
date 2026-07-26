def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b
def menu():
    print("WELCOME TO THE CALCULATOR")
    print("SELECT YOUR CHOICE:")
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    print("5. MOD")
    print("6. POW")
    print("7. Exit")
menu()
while True:
    option = int(input("Enter your choice: "))
    if option == 1:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        print("Result:",add(s,e))
    elif option == 2:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        print("Result:",sub(s,e))
    elif option == 3:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        print("Result:",mul(s,e))
    elif option == 4:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        if e == 0:
            print("Division by zero is not allowed")
        else:
            print("Result:",div(s, e))
    elif option == 5:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        if e == 0:
            print("Modulus by zero is not allowed")
        else:
            print("Result:",mod(s, e))
    elif option == 6:
        s = int(input("Enter a number: "))
        e=int(input("Enter a number: "))
        print("Result:",pow(s,e))
    elif option == 7:
        print("you are exiting function")
        break
    else:
        print("enter a valid option")
print("Thank You") 