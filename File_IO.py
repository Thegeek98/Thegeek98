# Open a File

f = open("Area_Of_Circle.py", "r")
print("Name of the file:", f.name)
print("Closed or not:", f.closed)
print("Opening mode:", f.mode)
f.close()
print("Closed or not:", f.closed)
# print("Softspace flag:", fo.softspace)
