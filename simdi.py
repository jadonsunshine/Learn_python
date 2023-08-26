n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    is_prime = True
    for num in range(2, n):
        if n % num == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
