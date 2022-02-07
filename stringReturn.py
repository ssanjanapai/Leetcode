class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle[0:len(needle)])

res=Solution()
r=res.strStr("disaster","ast")
print(r)