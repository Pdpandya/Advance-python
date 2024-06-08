from collections import deque

file=open("Twoo.txt","r+")
n = 1

line = deque(file,maxlen=n)

for last in line:
    print(last,end='')

file.close()