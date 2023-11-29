class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        for index, i in enumerate(s):
            if d.get(i) == 1:
                return index
        return -1