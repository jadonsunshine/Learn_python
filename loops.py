Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

UserName = input("Enter your First Name: ")
LenUsername = len(UserName)
print(f"Your Username has {LenUsername} letters. ")

Caps_UserName = UserName.upper()

def calculate():
    i = 0
    total = 0  # define total inside the function
    while i < LenUsername:
        index_of_alphabet = Alphabets.index(Caps_UserName[i])
        value = index_of_alphabet + 1
        total += value  # adding value to total
        i += 1
    return total  # return total from the function

total = calculate()  # assign the returned value to total
print(total)
