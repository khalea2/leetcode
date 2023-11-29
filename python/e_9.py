class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = str(x)
        backward = str(x)[::-1]
        if forward == backward:
            return True
        else:
            return False