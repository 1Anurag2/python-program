import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert all characters to lowercase
        s = s.lower()
        
        # Remove all non-alphanumeric characters
        s = re.sub(r'[^a-z0-9]', '', s)
        
        # Check if the string reads the same forward and backward
        return s == s[::-1]

# Example usage:
solution = Solution()

# Example 1
s1 = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s1))  # Output: True

# Example 2
s2 = "race a car"
print(solution.isPalindrome(s2))  # Output: False

# Example 3
s3 = " "
print(solution.isPalindrome(s3))  # Output: True
