# 8bit=1Byte
# integer value(unsigned,signed)
# unsigned(without - minus )
# unsigned bit = 32bits
# signed(can be + or - value)
# signed bit = 31bits

print("This program calculate for Signed and Unsigned values in bit")
print("************************************************************")
print()
print("signed=1")
print("unsigned=2")
bit = int(input("Please choose ( 1 or 2 ) = "))

if bit == 1 :
    val = ((2 ** 31) - 1)
    print("Unsigned Maximum value in bit: ", val)

elif bit == 2 :
    num = 31
    min = - (2**num)
    max = ((2**num) -1)
    print("Signed Minimum value in bit: ", min)
    print("Signed Maxmium value in bit: ", max)

else:
    print("Bad input!\n Please try again!!!")


