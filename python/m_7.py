class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        x = str(x)
        if s[0] == '-':
            s.pop(0)
            j = ''
            k = '-'
            for i in s:
                j += i
            for i in j[::-1]:
                k += i
            c = int(k)
        else:
            c = int(x[::-1])
        if c > 2**31 or c < -2**31:
            return 0
        else:
            return c
