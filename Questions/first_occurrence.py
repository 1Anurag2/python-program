class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
       
sol = Solution()
print(sol.strStr("sadbutsad","sad"))
print(sol.strStr("leetcode","leeto"))