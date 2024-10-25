
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
def findPairsWithGivenSum(head, target):
    if head is None:
        return head

    temp = head

    while temp.next is not None:
        if temp.data > target:
            break
        temp = temp.next
    
    ans = []
    left = head
    right = temp

    while left.data < right.data:
        sum = left.data + right.data
        if sum == target:
            ans.append([left.data, right.data])
            left = left.next
            right =  right.back

        elif sum > target:
            right =  right.back

        elif sum < target:
            left = left.next

    return ans
            



#######################################
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 9]
    head = array_to_list(arr)
    ans = findPairsWithGivenSum(head, 5)
    print(ans)
    display(head)