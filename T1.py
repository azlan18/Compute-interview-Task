n = int(input("Enter an integer: "))

if n % 2 == 1:  # Check if n is odd (remainder when divided by 2 is 1)
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:  # Check if n is even and in the range [2, 5]
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # Check if n is even and in the range [6, 20]
    print("Weird")
elif n % 2 == 0 and n > 20:  # Check if n is even and greater than 20
    print("Not Weird")
