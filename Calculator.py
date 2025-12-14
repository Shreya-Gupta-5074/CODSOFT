print("Welcome to simple calculating System")

while True:

    x=float(input("Enter the 1st digit: "))
    y=float(input("Enter the 2nd digit: "))

    print("Please select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Remainder\n"
        "6. Expotential or power\n"
        "7. Quotient \n")


    sign = int(input("select the parameter or sign(1,2,3,4,5,6,7): "))

    if sign == 1:
        print(x,"+", y ,"=", x+y)
    elif sign ==2:
        print(x,"-", y ,"=", x-y)
    elif sign ==3:
        print(x,"x", y ,"=", x*y)
    elif sign ==4:
        print(x,"/", y ,"=", x/y)
    elif sign ==5:
        print(x,"of", y, "remainder is =", x%y)
    elif sign ==6:
        print(x,"^", y ,"=", x**y)
    elif sign ==7:
        print(x,"//", y ,"=", x//y)
    else:
        print("Invalid Parameter")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again == "no":
        print("THANK YOU!")
        break