# you have to put this program in same folder

inpfile = open(input("Enter your file name: "))
redfile = inpfile.read()
file2l = redfile.split()
cwords = len(file2l)
print("Total words: ", cwords)
