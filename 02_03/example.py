# Function to reverse a string
def reverse_string(s):
    """
    Reverse the input string and return it.
    """
    return s[::-1]

# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    """
    Return the maximum of three given numbers.
    """
    return max(a, b, c)

# Function to calculate the sum of a list of numbers
def sum_of_list(numbers):
    """
    Return the sum of all elements in a list of numbers.
    """
    total = 0
    for number in numbers:
        total += number
    return total

# Function to check if a word is a palindrome
def is_palindrome(word):
    """
    Check if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    """
    return word == word[::-1]

# Test cases to check the functions
def test_functions():
    # Test reverse_string
    print("Testing reverse_string:")
    print(f"reverse_string('hello') = {reverse_string('hello')}")  # Should return 'olleh'

    # Test max_of_three
    print("\nTesting max_of_three:")
    print(f"max_of_three(10, 20, 15) = {max_of_three(10, 20, 15)}")  # Should return 20

    # Test sum_of_list
    print("\nTesting sum_of_list:")
    print(f"sum_of_list([1, 2, 3, 4, 5]) = {sum_of_list([1, 2, 3, 4, 5])}")  # Should return 15

    # Test is_palindrome
    print("\nTesting is_palindrome:")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")  # Should return True
    print(f"is_palindrome('hello') = {is_palindrome('hello')}")  # Should return False

# Run the tests
test_functions()
