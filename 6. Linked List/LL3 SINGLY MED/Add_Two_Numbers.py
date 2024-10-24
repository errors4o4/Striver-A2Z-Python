import math


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

def Add_2(l1, l2):
    t1 = l1
    t2 = l2
    dummy = Node(-1)
    curr = dummy
    carry = 0
    
    while (t1 is not None or t2 is not None) or carry:
        sum = carry
        if t1 != None: 
            sum += t1.data
            t1 = t1.next
        if t2 != None:
            sum += t2.data
            t2 = t2.next

        
        carry = sum//10
        newNode = Node(sum%10)

        curr.next = newNode
        curr = curr.next


    return dummy.next
#############################################################
# Driver code
if __name__ == "__main__":
    l1 = [3, 5]
    l2 = [4, 5, 9, 9]
    l1 = array_to_list(l1)
    l2 = array_to_list(l2)
    # head = Find_Middle(head)
    head = Add_2(l1, l2)
    display(head)
