Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

UserName = input("Enter your First Name: ")
LenUsername = len(UserName)
print(f"Your Username has {LenUsername} letters.")

Caps_UserName = UserName.upper()


def calculate():
    i = 0

    value_of_each_letter = 0
    while i < LenUsername:

        index_of_alphabet = Alphabets.index(Caps_UserName[i])
        value = index_of_alphabet + 1
        value_of_each_letter += value
        i += 1
    return value_of_each_letter


total = calculate()
print(f"Your Name's Numeric value is {total}")
