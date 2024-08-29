class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Reverses the input list of characters in-place.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the characters in the list
            s[left], s[right] = s[right], s[left]
            
            # Move the pointers towards the center
            left += 1
            right -= 1


s1 = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s1)
print(s1)  


s2 = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s2)
print(s2) 