class Solution:
    def twoSum(self,nums:list[int],target:int) -> list[int]:
        result = {}
        for i , num in enumerate(nums):
            component = target-num
            if component in result:
                return (result[component],i)
            result[num] = i
sol = Solution()
print(sol.twoSum([2,7,11,15],9)) 
print(sol.twoSum([4,5,26,3,2],7))
