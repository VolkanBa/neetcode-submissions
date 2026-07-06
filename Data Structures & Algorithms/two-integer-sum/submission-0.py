#i und j müssen zusammen target ergeben
#i darf nicht gleich j sein
#wenn i und j = target, dann speicher i und j in einer Liste bestehend aus diesen Werten
#doppelte schleife um zu testen
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoValues = []

        i = 0
        j = i + 1
        while i < len(nums):
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    twoValues.append(i)
                    twoValues.append(j)
                j += 1
            i+= 1
            j = i + 1
        return twoValues

