import random

lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?', '/', '~', '`']

length_lowercase_alphabet = int(input('How many lowercase letters do you want to be in your password? '))
length_uppercase_alphabet = int(input('How many uppercase letters do you want to be in your password? '))
length_numbers = int(input('How many numbers do you want to be in your password? '))
length_special_characters = int(input('How many special characters do you want to be in your password? '))

random_lowercase_alphabet = random.choices(lowercase_alphabet, k=length_lowercase_alphabet)
random_uppercase_alphabet = random.choices(uppercase_alphabet, k=length_uppercase_alphabet)
random_numbers = random.choices(numbers, k=length_numbers)
random_special_characters = random.choices(special_characters, k=length_special_characters)

total_password = random_lowercase_alphabet + random_uppercase_alphabet + random_numbers + random_special_characters
random.shuffle(total_password)
print(''.join(total_password))
