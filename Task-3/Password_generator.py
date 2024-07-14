#importing libraries
import random
import string

# Taking the user's input for defining the lenght of the password
length = int(input("Enter the length of the password: "))

# Defining the possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generating password using a for loop
password = ''
for _ in range(length):
    password += random.choice(characters)


# Displaying the generated password
print(f"Generated password: {password}")
