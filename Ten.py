from collections import Counter

file = open("Twoo.txt", "r")
text = file.read()
text = text.lower()

word = ''
words = []

for char in text:
    if char.isalnum(): 
        word += char
    else: 
        words.append(word)
        word = ''
    
w = Counter(words)

for word, count in w.items():
    print((word),":", (count))
