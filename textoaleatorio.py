import random
import colorama
from colorama import Fore, Style
chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン1234567890"
# diego alejandro 
print(Fore.RED + 'Diego Alejandro')

while True:
    key_len = int(input("What length would you like your key to be?: "))
    key_count = int(input("How many keys would you like?: "))
# diego alejandro 
    with open("generated_keys.txt", "a") as file:
        for _ in range(key_count):
            key = ""
            for _ in range(key_len):
                key_char = random.choice(chars)
                key += key_char
            print("Here's your key: ", key)
            file.write(key + "\n")

    print(Fore.CYAN + 'By Diego Alejandro')
    print(Fore.GREEN+ ' /////////////// ')
