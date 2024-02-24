"""
Program:
    Generates Random Passwords based on the Length the User's Desire.
"""

# import random, import string
import random
import string

# create string of random characters
PasswordOriginal = string.ascii_letters+string.digits+string.punctuation
# convert string into list
PasswordList = list(PasswordOriginal)

# shuffle list, convert list into string
random.shuffle(PasswordList)
PasswordNew = ''.join(PasswordList)

# create the Index Length of Character of Password
IndexLength = int(len(PasswordNew))-1;print("Password Generator v.2")

# ask the user the amount of characters the password will be
Amount = int(input("Length of Password (max:94chars): "))

# limit how many characters the user wants using indexing starting from 0
LimitPassword = PasswordNew[:Amount]

# output the information
print(LimitPassword)
