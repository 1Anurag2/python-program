class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Set to store numbers we've seen to detect cycles

        while n != 1 and n not in seen:
            seen.add(n)  # Add current number to the set
            n = sum(int(digit) ** 2 for digit in str(n))  # Calculate sum of squares of digits

        return n == 1  # If n becomes 1, it's a happy number, otherwise it's not

sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))         
        

        