# Function to calculate the factorial of a number
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    The factorial of n is the product of all positive integers less than or equal to n.
    For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    """
    Check if a number is prime.
    A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    For example, 7 is a prime number because it is only divisible by 1 and 7.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example function to add two numbers
def add_numbers(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

def max_of_three(a, b, c):
    """
    Find the maximum of three numbers.
    """
    return max(a, b, c)

# A function that calculates the max of five numbers
def max_of_five(a, b, c, d, e):
    """
    Find the maximum of five numbers.
    """
    return max(a, b, c, d, e)


# Test the functions
results = {
    "factorial_5": factorial(5),
    "factorial_0": factorial(0),
    "is_prime_7": is_prime(7),
    "is_prime_4": is_prime(4),
    "is_prime_1": is_prime(1),
    "add_numbers_3_5": add_numbers(3, 5),
    "add_numbers_-1_1": add_numbers(-1, 1),
    "max_of_three_3_7_5": max_of_three(3, 7, 5),
    "max_of_three_10_20_5": max_of_three(10, 20, 5)
}

for test, result in results.items():
    print(f"{test}: {result}")
    