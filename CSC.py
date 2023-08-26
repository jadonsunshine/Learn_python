numberOfCharacters = float(input("How many numbers are contained in this series : "))
series = []
firstNumber = input("input the first number in your series: ")
series.append(firstNumber)



isComplete = input("Do you still want to add number to your series: Enter 'Y' for Yes and 'N' for No:  ")
while isComplete == "y" or "Y":

    if "y" or "Y" == isComplete:
        numX = input("Enter another number in your series: ")
        series.append(numX)
        print(isComplete)

    elif "n" or "N" == isComplete:
        def average():
            total = 0
            for numbers in series:
                total += numbers
                print(total/numberOfCharacters)






