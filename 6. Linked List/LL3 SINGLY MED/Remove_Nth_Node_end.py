
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
def Remove_node(head,n):
    if head is None:
        return head

    temp = head
    count = 0

    while temp is not None:
        temp = temp.next
        count += 1

    if count == n:
        newhead = head.next
        head = None
        return newhead
    
    temp = head
    res = count-n
    
    while temp is not None:
        res -= 1
        if res == 0:
            break
        temp = temp.next

    delNode = temp.next
    temp.next = temp.next.next
    delNode = None

    return head
##################################################################

##################################################################
def Remove_node_2(head,n):
    if head is None:
        return head

    slow = head
    fast = head

    while n != 0:
        fast = fast.next
        n -= 1

    if fast is None:
        return head.next

    while fast.next is not None :
        slow=slow.next
        fast=fast.next

    delNode = slow.next
    slow.next = slow.next.next
    delNode = None
    return head
        


##################################################################
# Driver code
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head = Remove_node_2(head,5)
    display(head)
