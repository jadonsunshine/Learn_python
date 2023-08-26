# Ask the user for the number of elements
num_elements = int(input("Enter the number of elements in the series: "))

# Initialize an empty list to store the numbers
numbers = []

# Use a for loop to prompt the user for each number
for i in range(num_elements):
    while True:  # keep asking until a valid number is entered
        try:
            number = float(input("Enter number {}: ".format(i+1)))
            numbers.append(number)
            break  # exit the loop when a valid number is entered
        except ValueError:
            print("That's not a valid number, please try again.")

# Calculate and print the average
average = sum(numbers) / len(numbers)
print("The average of the numbers is: ", average)
while True:  # keep asking until a valid number is entered
    try:
        break  # exit the loop when a valid number is entered
    except ValueError:
        print("That's not a valid number, please try again.")