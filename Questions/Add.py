class Solution:
    def addSum(self,num : int) -> int:
        multiplier = num % 10
        remainder = num // 10
        sum = multiplier + remainder
        if (sum < 10):
            return sum
        else:
            return self.addSum(sum)
sol = Solution()
print(sol.addSum(38))

