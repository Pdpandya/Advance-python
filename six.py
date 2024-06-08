file = open("Twoo.txt", "r")
list =[]

for line in file:
    list.append(line)
  
print("Lines stored in list:")
#for line in list:
print(list)

file.close()