class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        length=len(nums)-len(s)
        list2=[]
        list2.append((length-1)*'_,')
        list2.append('_')
        list1=list(s)
        list3=[]
        list3=list1.extend(list2)
        print(list3)
        
        