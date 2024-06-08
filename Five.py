file = open("Twoo.txt", "r+")
l = None

for line in file:
    l = line 
if l:
    print(l, end='')

file.close()
