file = open("Twoo.txt", "r")
w = file.read().split()
m = 0
l = []

for word in w:
    if len(word) > m:
        m = len(word)
        l = [word] 
    elif len(word) == m:
        l.append(word)
print(l)

file.close()