class Node:

  def __init__(self, data):
    self.data = data 
    self.next = next


def insert(head, item):
  temp = Node(0)
  temp.data = item
  temp.next = head
  head = temp
  return head


def Del_head(head):
  temp = head.next
  head = temp

  return head


def arr2List(arr, n):
  head = None
  for i in range(n - 1, -1, -1):
    head = insert(head, arr[i])
  return head


def display(head):
  temp = head
  while (temp != None):
    print(temp.data, end=' ')
    temp = temp.next


#######################################
# WRITE CODE


#######################################


if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  head = arr2List(arr, n)
  # head = CALLFUNC()
  display(head)