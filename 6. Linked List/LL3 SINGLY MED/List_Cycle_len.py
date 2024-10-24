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
  if head is None:
    return 0

  mpp = {}
  temp = head
  count = 0

  while temp is not None:
    if temp in mpp:
      ans = count - mpp[temp]
      return ans

    mpp[temp] = count
    count += 1
    temp = temp.next

  return 0


####################################################################


####################################################################
def List_cycle_2_PO(head):
  if head is None or head.next is None:
    return 0

  slow = head
  fast = head

  while fast.next is not None and fast is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      count = 1
      fast = fast.next
      while slow != fast:
        count += 1
        fast = fast.next
      return count

  return 0


####################################################################

# Driver code
if __name__ == "__main__":
  arr = [3, 2, 0, -4]
  head = Node(arr[0])
  head.next = Node(arr[1])
  head.next.next = Node(arr[2])
  head.next.next.next = Node(arr[3])
  head.next.next.next.next = head.next
  head = List_cycle_2_PO(head)
  print(head)
