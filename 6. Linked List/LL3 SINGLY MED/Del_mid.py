
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
def Del_mid(head):
    if head.next is None:
        return head

    slow = head
    fast= head
    prev = None
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    delNode = prev.next
    prev.next = prev.next.next
    delNode = None

    return head
    
    

##################################################################
# Driver code
if __name__ == "__main__":
    head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)
    # head = Del_mid(head)
    display(head)
