class Solution:
    def removeDuplicates(self,nums) -> int:
        s=set(nums)
        length=len(nums)-len(s)
        list2=[]
        list2.append(length)
        list3=[]
        list3=list2 + list(s)
        return list3

c=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
r=c.removeDuplicates(nums)
print(r)

'''
output in the form [no. of repeated elements , 
remaining elements after eliminating repeated elements
'''

'''
example:
nums=[0,0,1,1,1,2,2,3,3,4]
no. of repeated elements (0,1,1,2,3)= 5  -----> (1)
elements remaining after removing 0,1,1,2,3= 0,1,2,3,4 ----->(2)
output=[(1),(2)] ===> [5, 0, 1, 2, 3, 4]
'''
