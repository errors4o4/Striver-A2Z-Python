
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
def sort(head):
    if head is None or head.next is None:
        return head

    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next

    arr.sort()
    temp = head
    for i in range(len(arr)):
        temp.data = arr[i]
        temp = temp.next

    return head

##################################################################

def findMiddle(head):
  if head is None and head.next is None:
    return head

  slow = head
  fast = head.next

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow

#######

def mergeTwoSortedLinkedLists(list1, list2):
    dummyNode = Node(-1)
    temp =dummyNode

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next=list2
            list2=list2.next

        temp = temp.next

    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2

    return dummyNode.next

#######

def sort_merge(head):
    if head is None or head.next is None:
        return head

    middle = findMiddle(head)
    
    leftHead= head
    rightHead = middle.next
    middle.next = None
    
    leftHead = sort_merge(leftHead)
    rightHead =sort_merge(rightHead)

    return mergeTwoSortedLinkedLists(leftHead, rightHead)
    
##################################################################
# Driver code
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(5)
    head = sort_merge(head)
    display(head)
