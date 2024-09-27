def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome')