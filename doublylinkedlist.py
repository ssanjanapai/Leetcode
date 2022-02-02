class Node: 
    #Defining a node
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self) -> None:
        self.head=None

fisrtNode = Node(3)
secNode = Node(4)
thirdNode = Node(8)
fourthNode = Node(9)

fisrtNode.next = secNode
secNode.next = thirdNode
secNode.prev = fisrtNode
thirdNode.prev = secNode
thirdNode.next = fourthNode
fourthNode.prev = thirdNode

'''List looks like

3 <---> 4 <--> 8 <--> 9

'''


dll_obj = DLL()
dll_obj.head = fisrtNode

tmp = dll_obj.head

# Linear traversal
while tmp is not None:
    print(tmp.data, end=" <--> ")
    if tmp.next is None:
        print("None")
    tmp=tmp.next

tmp_last = fourthNode

# Traversal in reverse order
while tmp_last is not None:
    print(tmp_last.data, end=" <--> ")
    if tmp_last.prev is None:
        print("None")
    tmp_last=tmp_last.prev
