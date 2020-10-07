#This is the Calculator Program by burmesegeek
#Programmer:    Zin Ko
#Date:          6.10.2020
while 1:
    first_no = float(input("Please enter first number:   "))
    operator = input("Please enter operator:   ")
    last_no = float(input("Please enter last number:   "))

    if operator == '+':
        result = first_no + last_no

    elif operator == '-':
        result = first_no - last_no

    elif operator == '*':
        result = first_no * last_no

    elif operator == '/':
        result = first_no / last_no

    elif operator == '%':
        result = first_no % last_no

    else:
        print('Wrong Operator')

    print('Your answer is ', result)

