Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Alphabets_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. user should input value
# 2. te value should be calculated to get the index
# 3. index should be added to 1 to get the position

value = input(str("Enter your Alphabet: "))

def calculatePosition():
    if (value.isupper()):
        indexOfAlphabet = Alphabets.index(value)
    elif (value.islower()):
        indexOfAlphabet = Alphabets_lower.index(value)

    print(indexOfAlphabet + 1)

calculatePosition()