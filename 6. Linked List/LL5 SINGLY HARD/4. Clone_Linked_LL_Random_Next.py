
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random

#######################################################
# BRUTE-FORCE
# HASHMAP

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if head is None:
        return head 

    mpp = {}
    temp = head

    while temp is not None:
        copy = Node(temp.val)
        mpp[temp] = copy 
        temp = temp.next


    temp = head
    while temp is not None:
        cpNode = mpp[temp]
        cpNode.next = mpp.get(temp.next, None)
        cpNode.random = mpp.get(temp.random, None)
        temp = temp.next

    return mpp[head]


#######################################################
# OPTIMAL
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if head is None:
        return head 

    temp = head
    while temp is not None:
        newNode = Node(temp.val)
        newNode.next = temp.next
        temp.next = newNode
        temp = temp.next.next

    temp = head
    while temp is not None:
        cp = temp.next
        if temp.random != None:
            cp.random = temp.random.next 
        else:
            cp.random =  None
        temp = temp.next.next 

    temp = head
    dummyNode = Node(-1)
    res = dummyNode
    while temp is not None:
        res.next = temp.next
        temp.next = temp.next.next

        res = res.next
        temp = temp.next

    return dummyNode.next
 