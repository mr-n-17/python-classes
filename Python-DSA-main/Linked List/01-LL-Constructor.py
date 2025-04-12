class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinledList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


my_lnkedlist=LinledList(4)
print('Head',my_lnkedlist.head.value)
print('Tail',my_lnkedlist.tail.value)
print('Length',my_lnkedlist.length)