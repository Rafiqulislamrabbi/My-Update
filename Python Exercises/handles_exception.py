try:
  age = int(input('what is your age : '))
  print(age)

except ValueError:
  print('Invalid value')