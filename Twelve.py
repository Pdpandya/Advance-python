data = ["First line", "Second line", "Third line", "Fourth line"]

file = open("eleven.txt", "w") 
for item in data:
    file.write(item + "\n")

print(file)
