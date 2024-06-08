file = open("Twoo.txt", "r")

w = file.read().split()
length = max(len(word) for word in w)
l_word = [word for word in w if len(word) == length]

  
print("Lines stored in Variable:")

print(l_word)

file.close()