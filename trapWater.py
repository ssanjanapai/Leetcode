class Solution:
    def maxArea(self, height) -> int:
        if len(height) <= 1:
            return 0
        ret = 0
        left, right = 0, len(height)-1
        while left < right:
            tmp = (right-left)*min(height[left], height[right])
            ret = max(tmp, ret)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ret

res=Solution()
r=res.maxArea([1,8,6,2,5,4,8,3,7])
print(r)
        