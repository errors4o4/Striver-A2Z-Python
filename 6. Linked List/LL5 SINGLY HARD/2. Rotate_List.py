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

#############################################################
def rotateRight(head, k):
    if head == None or head.next == None or k == 0 :
        return head

    temp = head
    lenn = 1 
    while temp.next != None: 
        lenn += 1
        temp = temp.next

    temp.next = head
    k = k % lenn
    end = lenn -k 

    while end != 0:
        temp = temp.next
        end -= 1
        
    head = temp.next
    temp.next = None

    return head
        


#############################################################
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3,4,5]
    k = 2
    head = array_to_list(arr)
    head = rotateRight(head, k)
    # print(rotateRight(head, k))
    display(head)
