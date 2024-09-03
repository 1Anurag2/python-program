class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = s.translate(str.maketrans("","",".,:"))
        nospace = "".join(char.split())
        # print(nospace)
        small = nospace.lower()
        # print(small)

        reversetext = small[::-1]
        if (small == reversetext):
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
