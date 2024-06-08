file = open("Twoo.txt", "r")
a =""

for line in file:
    a += line
  
print("Lines stored in list:")
#for line in list:
print(a)

file.close()