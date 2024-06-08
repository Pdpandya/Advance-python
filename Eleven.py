
file = open("Twoo.txt", "r")
a = ""
for line in file:
    a += line

print("Lines stored in variable:")
print(a)

# Writing the contents to the output file
ofile = open("output.txt", "w")
ofile.write(a)

print(ofile)

