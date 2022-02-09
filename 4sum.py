class Solution:
    def fourSum(self, nums, target): #output in format: List[List[int]]
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]+nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                
                        left += 1
                        right -= 1
        return ans

res=Solution()
r=res.fourSum([1,0,-1,0,-2,2],0)
print(r)