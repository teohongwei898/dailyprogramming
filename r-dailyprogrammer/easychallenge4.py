import random

foo = int(input("How many passwords do you wish to generate? "))
bar = int(input("How many characters should each password have? "))
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
result = ''

for a in range(foo):
    for b in range(bar):
        place = random.randint(0, len(chars) - 1)
        result = result + chars[place]

    print(result)
    result = ''
