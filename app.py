print("Hello World") 
name = "Jadon"
print(name);
birthyear = int(input("Enter your birth year :   "))
age = 2023 - birthyear
print(age)

# now lets build a simple calculator
first_Number = float(input("Please input first number: "));
second_Number = float(input("Please input second number: "));
Add = first_Number + second_Number;
result = "Sum : "+ str(Add)
print(result)
# Powerful things to do with Strings

course = "Python for the Weak"
# course.differentmethod
# course.upper : to uppercase
# course.lower:to lowercase
# course.find to find a specific character or word in you code
course.replace("for", "4")
print(course)
print(course.replace("for", "4"))
# in operator
print("Python" in course)

# operators in Python
# add : a + b
# sub : a - b
# mult : a * b
# power : a ** b
# float(div) : a / b
# int(div) : a // b
# modulus : a % b

# argumented assignment operator{
# x = 10
# x = x + 3
# argumented assignment operator : x += 3}

# //Python also makes use of bool operators like:
# and price > 20 and market_value <20
# or price > 20 or market_value <20
# not  market_value <20

# //If statement in Python
temperature = 30
if temperature >30:
        print("it's a hot day")
        print("drink plenty of water")

elif temperature > 20 :
        print("it's a nice day")
       
elif temperature > 20 :
        print("it's a hot day")
        
else :
        print("it's a cold day")
       
