class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i in count.items():
            if i[1] > n / 2:
                return i[0]