from collections import Counter
import re

file = open("Twoo.txt", "r")
text = file.read()
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)

for word, count in word_count.items():
    print((word),":", (count))
