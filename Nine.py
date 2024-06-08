file = open("Twoo.txt", "r")

l = 0
for line in file:
    l += 1

print("Number of lines in the file:", l)
