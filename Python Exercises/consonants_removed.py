text = input('Enter text: ')

for char in text:
    if char.lower() in 'aeiou':
        print(char)   