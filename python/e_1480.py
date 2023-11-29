class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        ans = []
        for i in nums:
            x += i
            ans.append(x)
        return ans