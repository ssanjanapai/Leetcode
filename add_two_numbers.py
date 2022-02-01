# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2="",""
        while l1 or l2:
            if l1: 
                n1=n1+str(l1.val)
                l1=l1.next
            if l2: 
                n2=n2+str(l2.val)
                l2=l2.next
        
        n=str(int(n1[::-1])+int(n2[::-1]))
        l=ListNode(n[0])
        n=n[1:]
        while len(n)>=1:
            new=ListNode(n[0])
            new.next=l
            l=new
            n=n[1:]
        return l