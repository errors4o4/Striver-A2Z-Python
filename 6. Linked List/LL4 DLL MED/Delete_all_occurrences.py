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
def Del_key(head, key):
    if head is None:
        return head

    temp = head
    NewHead = head
    while temp is not None:
        if temp.data == key:

            if temp.back is None:
                front = temp.next
                front.back = None
                NewHead = front

            elif temp.next is None:
                prev = temp.back
                prev.next = None
            
            else:
                front = temp.next
                prev = temp.back
                prev.next = front
                front.back =prev
 
        temp= temp.next
    
    return NewHead
            

#######################################
# Driver code
if __name__ == "__main__":
    arr = [10, 4, 10, 10, 6, 10]
    head = array_to_list(arr)
    head = Del_key(head, 10)
    display(head)