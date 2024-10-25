
from re import template


class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back


def array_to_list(arr):
    n = len(arr)
    head = Node(arr[0])
    prev = head

    for i in range(1, n):
        temp = Node(arr[i], None,prev)
        prev.next = temp
        prev = temp
    return head


def display(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp =temp.next


#######################################
# WRITE CODE
# MY CODE
def removeDuplicates(head):  
    if head is None or head.next is None:
        return head

    temp = head
    front = head.next
    while front is not None:
        if temp.data != front.data:
            temp.next = front
            front.back = temp
            temp = front
                
        front = front.next

    temp.next = None
    
    return head
                

#######################################
# Driver code
if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3 , 3 , 4, 4]
    head = array_to_list(arr)
    head = removeDuplicates_str(head)
    display(head)