class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # another super smart way
        
        if not strs: return "" # <- although minimum one string, good to have
        
        # find min and max alphabetically fast
        strs.sort() 
        s1,s2= strs[0],strs[-1]

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] # if differing chars, return up till index
        return s1