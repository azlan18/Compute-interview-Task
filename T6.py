
def generate_fibonacci(n):
    fibonacci_list = [0, 1]  # Initializing the first two Fibonacci numbers
    while len(fibonacci_list) < n:
        next_num = fibonacci_list[-1] + fibonacci_list[-2]  #Computing the next Fibonacci number
        fibonacci_list.append(next_num)
    return fibonacci_list[:n]


n = int(input("Enter the value of n: "))

# Generating 'n' Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)

# Using map and lambda to cube each Fibonacci number
cubed_fibonacci = list(map(lambda x: x**3, fibonacci_numbers))

# Print the cubed Fibonacci numbers
print(cubed_fibonacci)
