#
# '''
# Numerologists claim to be able to determine a person’s character traits based on the
# “numeric value” of a name. The value of a name is determined by summing up the
# values of the letters of the name where "a" is 1, "b" is 2,"c" is 3 etc., up to "z" being
# 26. For example, the name “Zelle” would have the value 26 + 5 + 12 + 12 + 5 = 60.
# Write a program that calculates the numeric value of a single name provided as
# Input
# '''
# Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#
# UsersName = input("Enter your firstname: ")
# Name = UsersName.upper
# print(Name)
#
# def calcNumValue():
#     return "hi"
# # Alphabets[5] = "f"
#
# for letter in Alphabets:
#   print(index(F, Alphabets))

##############Isreals thoughts
print("Alphabet to Position")
Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

value = input("Enter alphabet: ")
value.upper
indexOfAlphabet = Alphabets.index(value)

print(indexOfAlphabet + 1)
