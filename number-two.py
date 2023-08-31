Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

UserName = input("Enter your First Name: ")
LenUsername = len(UserName)
print(f"Your Username has {LenUsername} letters. ")

Caps_UserName = UserName.upper()

total = 0
def calculate():
    value = 0
    for letter in Caps_UserName:
        index_of_alphabet = Alphabets.index(letter) + 1
        value += index_of_alphabet
    return value
total += calculate()
print(f"Your Name's Numeric value is {total}")
