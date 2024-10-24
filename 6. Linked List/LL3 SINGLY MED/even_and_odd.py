
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
def Segregate_hash(head):
  if head is None:
    return head

  if head.next is None:
    return head

  hash = []
  temp = head

  while temp is not None:
    hash.append(temp.data)
    temp = temp.next.next

  temp = head.next
  while temp.next is not None:
    hash.append(temp.data)
    temp = temp.next.next

  start = head
  for ele in hash:
    start.data = ele
    start = start.next

  return head


##################################################################


def Segregate_LL(head):
  if head is None or head.next is None:
    return head

  odd = head
  even = head.next
  evenhead = head.next

  while (even != None and even.next != None):
    odd.next = odd.next.next
    even.next = even.next.next

    odd = odd.next
    even = even.next

  odd.next = evenhead

  return head


a = [1, 3, 4, 2, 5, 6]

##################################################################
# Driver code
if __name__ == "__main__":
  head = Node(1)
  head.next = Node(3)
  head.next.next = Node(4)
  head.next.next.next = Node(2)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head = Segregate_LL(head)

  display(head)
