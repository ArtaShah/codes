class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)
        n= len(haystack)
        m= len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]== needle:
                return i
        return -1
