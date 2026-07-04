class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doubles = False 
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                doubles = True
                break
            i += 1 
        return doubles