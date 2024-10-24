


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

def sort012(head):
    if head is None or head.next is None:
        return head

    zeroDummy = Node(-1)
    oneDummy = Node(-1)
    twoDummy = Node(-1)

    zero = zeroDummy
    one = oneDummy
    two = twoDummy

    temp = head
    while temp is not None:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next

        elif temp.data == 1:
            one.next =  temp
            one = one.next

        else:
            two.next =  temp
            two = two.next

        temp = temp.next

    if oneDummy.next is not None:
        zero.next = oneDummy.next
        one.next = twoDummy.next
    else:
        zero.next = twoDummy.next

    two.next = None

    return zeroDummy.next
            
    


##################################################################
# Driver code
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(0)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(0)
    head = sort012(head)
    display(head)
