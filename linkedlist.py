class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class SinglyLinked:
    def __init__(self) -> None:
        self.head=None

'''Creating the following linkedlist

|2|-->|8|-->|9|-->|7|

'''

firstNode=Node(2)
secNode=Node(8)
thirdNode=Node(9)
fourthNode=Node(7)

#for head pointer - to point to first element:

sll_obj=SinglyLinked()
sll_obj.head=firstNode

'''|2|-|-->|8|-|-->|9|-|-->|7|None|
    ^
    |    
    head-pointer
'''

firstNode.next=secNode
secNode.next=thirdNode
thirdNode.next=fourthNode

tmp=sll_obj.head

while tmp != None:
    print(tmp.data,end=" ")
    tmp=tmp.next



    