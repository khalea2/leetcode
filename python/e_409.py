class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s: 
            d[i] = d.get(i, 0) + 1
        length, odd_found = 0, False
        for _, c in d.items():
            if c % 2 == 0:
                length += c
            else:
                odd_found = True
                length += c - 1
        if odd_found: length += 1
        return length
