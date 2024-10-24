class Node:

    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def insert_end(head, item):
    temp = Node(item)
    if head is None:
        return temp  # temp means new head

    last = head
    while last.next is not None:
        last = last.next

    last.next = temp
    return head


def array_to_list(arr):
    head = None
    for item in arr:
        head = insert_end(head, item)
    return head


def display(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


####################################################################


def Intersection(headA, headB):
    if headA is None or headB is None:
        return None

    mpp = {}

    tempA = headA
    while tempA is not None:
        mpp[tempA] = True
        tempA = tempA.next

    tempB = headB
    while tempB is not None:
        if tempB in mpp:
            return tempB
        tempB = tempB.next

    return None


##################################################################

##################################################################


def Intersection_Move(headA, headB):
    if headA is None or headB is None:
        return None

    NA = 0
    NB = 0

    tempA = headA
    while tempA is not None:
        NA += 1
        tempA = tempA.next

    tempB = headB
    while tempB is not None:
        NB += 1
        tempB = tempB.next

    tempA = headA
    tempB = headB
    if NA <= NB:
        NB = NB - NA
        while NB != 0:
            NB -= 1
            tempB = tempB.next
            
    else:
        NA = NA - NB
        while NA != 0:
            NA -= 1
            tempA = tempA.next

    while tempA is not None:
        if tempA == tempB:
            return tempA.data
        tempA = tempA.next
        tempB = tempB.next

    return None
        
##################################################################

##################################################################
def Intersection_Cycle(headA, headB):
    if headA is None or headB is None:
        return None

    tempA = headA
    tempB = headB

    while tempA != tempB:
        tempA = tempA.next
        tempB = tempB.next

        if tempA == tempB: 
            return tempA

        if tempA == None:
            tempA=headB
            
        if tempB == None:
            tempB=headA
        
    return tempA

    
        

##################################################################
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    head = array_to_list(arr)
    display(head)
