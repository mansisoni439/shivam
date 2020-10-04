# calculator for checking exe file
rotate = True
print("      valid operation")
print(" ")
print(r"for addition           +")
print("for substraction        -")
print("for multiplicattion     *")
print("for division            /")
print("for power               **")
print("for remainder           %")
print(" ")

while(rotate == True):
    print(" ")
    a = float(input("Enter your First value : "))
    b = str(input("Operation : "))
    c = float(input("Enter your second value : "))
    if(b == '+'):
        print(f"The addition of {a} and {c} is {a+c}")
    elif(b == '-'):
        print(f"The substraction of {a} and {c} is {a - c}")
    elif(b == '*'):
        print(f"The multiplication of {a} and {c} is {a * c}")
    elif(b == '/'):
        print(f"The division of {a} and {c} is {a / c}")
    elif(b == '**'):
        print(f"The power of {a} by {c} is {a ** c}")
    elif(b == '%'):
        print(f"The remainder of {a} by {c} is {a % c}")
    else:
        print("Invalid Input")

    print(" ")
    print("You wanna continue press     Y")
    print("You wanna exit press         N")

    conti = str(input("press y/n : "))
    if(conti == "Y" or conti == "y"):
        rotate = True
    elif(conti == "n" or conti == "n"):
        rotate = False
    else:
        print("invalid Input")
        print("restart program")
        exit()
