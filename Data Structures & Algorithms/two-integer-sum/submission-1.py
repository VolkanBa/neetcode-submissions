#In einer HashMap lösbar. Man guckt ob Ergebnis - Zahl in HashMap. Wenn nicht fügt man Zahl in HashMap
#Das macht man so lange bis Array zuende ist oder Wert gefunden wurde
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         hashMapSave = {}

         for index, num in enumerate(nums):
            searchedNum = target - num
            if searchedNum in hashMapSave:
                return [hashMapSave[searchedNum], index]
            hashMapSave[num] = index

