class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[count] = nums[i]
                count+=1
        return count

res=Solution()
r=res.removeElement([3,2,2,3],3)
#3 is to be removed
print(r)