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

def Add(head):
    if head is None:
        return head

    head = Rev_list(head)
    temp = head
    carry = 1
    
    while temp is not None:
        temp.data += carry
        
        if temp.data < 10:
            carry= 0
            break     
        else:
            temp.data = 0
            carry = 1
                
        temp = temp.next
            
    if carry == 1:
        newNode = Node(1)
        head = Rev_list(head)
        newNode.next = head
        return newNode
    
    head = Rev_list(head)
    return head
#############################################################
            
#############################################################

def carry_helper(temp):
    if temp is None:
        return 1

    carry = carry_helper(temp.next)
    temp.data += carry
    if temp.data < 10:
        return 0
    else:
        temp.data = 0
        return 1
    

def Add_Ruc(head):
    if head is None:
        return head
    carry=carry_helper(head)
    
    if carry ==  1:
        newNode = Node(1)
        newNode.next = head
        return newNode
    else:
        return head
        

#############################################################
# Driver code
if __name__ == "__main__":
    arr = [9, 9, 9]
    head = array_to_list(arr)
    # head = Find_Middle(head)
    head = Add_Ruc(head)
    display(head)
