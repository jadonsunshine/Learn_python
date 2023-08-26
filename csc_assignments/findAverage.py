while True:
    try:
        numberOfCharacters = int(input("How many numbers are contained in this series: "))
        break
    except ValueError:
        print("That's not a valid number, please try again.")

print(f'The number of Character in your series is {numberOfCharacters} ')
series = []

while True:
    try:
        firstNum = int(input("Enter the First number in your series: "))
        break
    except ValueError:
        print("That's not a valid number, please try again.")
series.append(firstNum)
i = 0
while i < numberOfCharacters - 1:
    while True:
        try:
            numX = int(input(f"Enter number { i + 2 } in your series: "))
            break
        except ValueError:
            print("That's not a valid number, please try again.")

    series.append(numX)
    i += 1
print(series)
sumOfSeries = 0
for number in series:
    sumOfSeries += number
average = sumOfSeries / numberOfCharacters
print(f"The average of the series is: {average}")
