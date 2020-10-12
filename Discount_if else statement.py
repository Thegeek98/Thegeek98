#This is an example of if ... else statement
#Programmer :   Zin Ko
#Date :         6.10.2020

while 1:

    amount=int(input("Please enter amount: "))
    if amount < 1000 :
        discount = amount * 0.05
        print("Discount", discount)

    elif amount < 5000 :
        discount = amount * 0.10
        print("Discount", discount)

    else :
        discount = amount * 0.10
        print("Discount", discount)
    print("Net payble: ", amount - discount)