file = open("Twoo.txt", "r")
list =[]

for line in file:
    list.append(line)
  
print(list)

file.close()