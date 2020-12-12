numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == 'Done':
        break
    value = float(inp)
    numlist.append(value)
avg = sum(numlist) / len(numlist)
print("Total values: ", sum(numlist))
print("Total avg: ", avg)
