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


#############################################################
# NORMAL METHOD
def Rev_list(head):
    if head is None and head.next is None:
        return head

    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev

#############################################################

def KthNode(temp, k):
    k -= 1 
    while temp is not None:
        if k == 0:
            return temp
        k -= 1 
        temp = temp.next
    return None


#############################################################
def reverseKGroup(head, k):
    if head is None:
        return head

    temp = head
    prevNode = None
    while temp is not None:
        Kth = KthNode(temp, k)

        if Kth == None:
            if prevNode != None:
                prevNode.next = temp
            break
        
        NextNode = Kth.next
        Kth.next = None

        newHead = Rev_list(temp)

        if temp == head:
            head = Kth
        else:
            prevNode.next = Kth

        prevNode = temp
        temp = NextNode  

    return head    
        
        


#############################################################
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = array_to_list(arr)
    # head = Find_Middle(head)
    head = reverseKGroup(head, 3)
    display(head)
