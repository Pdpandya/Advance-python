file=open("Twoo.txt","r+")
n = 1
for i in range(n):
    line = file.readline()
    print(line,end='')

file.close()