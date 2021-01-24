# This is

print("Welcome to ZinKO's online banking service!\nFirst, you need to create a new acc to join the community.")
print("Here, there are the acc types we offer:")
print("1: Simple common acc\t\t\n2. Underage acc\t\t\n3. Long time acc")
a = " Simple common acc "
b = " Underage acc "
c = " Long time acc "
udata = int(input("Choose the number of service that you want: "))
if udata == 1:
    con = input("You choose to pick service num: 1 \nEnter 'yes' to confirm and 'no' to cancel: ")
    if con == 'yes':
        print("Thank for choosing Simple acc.\nHere's the benefit of this service: You can withdraw your money at " +
              "every bank's MPU with the specific charge.")
    elif con == 'no':
        print("You have cancelled.")
    else:
        print("Choose only: 'yes' or 'no' ")

elif udata == 2:
    con = input("You choose to pick service num: 2 \nEnter 'yes' to confirm and 'no' to cancel: ")
    if con == 'yes':
        print("Thank for choosing Underage acc.\nBut you need to be underage and your money can only be withdrawed when"
              + " you are adult.\nAnd the interest rate is 5%")
    elif con == 'no':
        print("You have cancelled.")
    else:
        print("Choose only: 'yes' or 'no' ")

elif udata == 3:
    con = input("You choose to pick service num: 3\nEnter 'yes' to confirm and 'no' to cancel: ")
    if con == 'yes':
        print("Thank for choosing Long time acc.\nYou can only withdraw your money over a specific of time.\nHere's our"
              + "interest rate amount:\n1.Over 3 years:\t6.5%\n2.Over 5 years\t8%\n3.Over 7 years")
    elif con == 'no':
        print("You have cancelled.")
    else:
        print("Choose only: 'yes' or 'no'")