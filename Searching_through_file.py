hand = open(input("Enter File Name: "))
for line in hand:
    line = line.rstrip()  # if you don't add print will add extra blink line
    if line.startswith('From: '):
        print()

# You can write this way

hand = open(input("Enter File Name: "))
for line in hand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)

# Using in to Select lines

hand = open(input("Enter File Name: "))
for line in hand:
    line = line.rstrip()
    if not "From" in line:
        continue
    print(line)

# for bad file names

hand = input("Enter File Name: ")
try:
    hand = open(hand)
except:
    print('File cannot be opened:', hand)
    print('May be "Wrong Name" or "Corrupted')
    quit()

for line in hand:
    line = line.rstrip()
    if not "From" in line:
        continue
    print(line)
