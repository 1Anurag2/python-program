class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nospace = s.strip()
        words = s.split()
        if words:
            return len(words[-1])

        else:
            return 0
sol = Solution()
s1 = "Hello World"
print(sol.lengthOfLastWord(s1))

s2 = "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s2))

s3 = "luffy is still joyboy"
print(sol.lengthOfLastWord(s3))