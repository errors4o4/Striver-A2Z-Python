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
def Find_Middle(head):
  if head is None:
    return None

  if head.next is None:
    return head

  count = 0
  temp = head
  while temp.next is not None:
    count += 1
    temp = temp.next

  mid = math.ceil(count / 2)
  temp = head

  count = 0
  while count != mid:
    count += 1
    temp = temp.next

  return temp


#############################################################


def Find_mid_opt(head):
  if head is None and head.next is None:
    return head

  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow


#############################################################

# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4]
  head = array_to_list(arr)
  # head = Find_Middle(head)
  head = Find_mid_opt(head)
  display(head)
