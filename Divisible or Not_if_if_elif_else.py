#This program is if inside if statement
#Programmer :   Zin Ko
#Date :         6.10.2020

num = int(input("Please enter number: "))
if num%2 == 0 :
    if num%3 == 0 :
        print("This number can be devided by 2 or 3")
    else :
        print("This number can be devided by 2")

else:
    if num%3 == 0 :
        print("This number can be devided by 3")
    else :
        print("This number can't be devided by 2 or 3")

