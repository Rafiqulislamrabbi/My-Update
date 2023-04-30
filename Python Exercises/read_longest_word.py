filename = "example.txt"

with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    longest_word = max(words, key=len)

print("The longest word is:", longest_word)