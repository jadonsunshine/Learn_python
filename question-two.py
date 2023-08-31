print("Alphabet to Position")
Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

UserName = input("Enter your First Name: ")
print(f"Your Username has {len(UserName)} letters.")

Caps_UserName = UserName.upper()

def calculate():
    total = 0
    for letter in Caps_UserName:
        value = ord(letter) - 64  # get the value of the letter
        total += value  # add the value to total
    return total

total = calculate()
print(f"Your Name's Numeric value is {total}")
