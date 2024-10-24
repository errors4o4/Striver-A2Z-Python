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
def List_cycle(head):
  mpp = {}

  temp = head
  while temp.next is not None:
    if temp.next in mpp:
      return True

    mpp[temp.next] = temp.data
    temp = temp.next

  return False


####################################################################


####################################################################
def List_cycle_2_PO(head):
  if head is None or head.next is None:
    return False

  slow = head
  fast = head

  while fast.next is not None and fast is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True

  return False


####################################################################

# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  display(head)
