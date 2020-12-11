# This is the counting line program by Zin KO
# Programmer    : Zin KO
# Date          : 11.11.2020

# You have to put this program to same directory to file that you count
counting = open(input("Enter File Name: "))
count = 0
for testing in counting:
    count = count + 1
print("Total number of line: ", count)
