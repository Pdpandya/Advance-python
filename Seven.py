file = open("Twoo.txt", "r")
a =""

for line in file:
    a += line
  
print(a)

file.close()