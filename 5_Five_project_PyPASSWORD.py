import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_how_many = int(
  input("How many letters would you like in yours password?\n"))
symbols_how_many = int(input("How many symbols would you like?\n"))
numbers_how_many = int(input("How many numbers would you like?\n"))

ready_pass = []

for char in range(letters_how_many):
  ready_pass.append(random.choice(letters))

for char in range(symbols_how_many):
  ready_pass.append(random.choice(symbols))

for char in range(numbers_how_many):
  ready_pass.append(random.choice(numbers))

random.shuffle(ready_pass)

password = ''.join(ready_pass)

print(password)

