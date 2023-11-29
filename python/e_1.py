class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, first in enumerate(nums):
            for index2, second in enumerate(nums):
                print(index1, first, index2, second)
                if index1 == index2:
                    pass
                elif first + second == target:
                    return [index1, index2]