class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        # Define the window range, left l and right r
        l = r = 0
        max_len = 0
        while r < len(s):
            # Update l if duplicates found, note l will never move left
            if d.get(s[r], None) is not None:
                l = max(l, d.get(s[r]) + 1)
            d[s[r]] = r
            r += 1
            max_len = max(max_len, r-l)
        return max_len

res=Solution()
r=res.lengthOfLongestSubstring("abcabcbb")
print(r)