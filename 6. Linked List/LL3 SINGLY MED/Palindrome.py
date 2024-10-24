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
def Palindrome_hash(head):
  if head is None and head.next is None:
    return False

  hash = []
  temp = head
  while temp is not None:
    hash.append(temp.data)
    temp =temp.next

  temp = head
  while temp  is not None:
    if temp.data != hash[-1]:
      return False
    hash.pop()
    temp =temp.next

  return True
####################################################################

####################################################################
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
####################################################################
def Palindrome_hash_2_PO(head):
  if head is None and head.next is None:
    return False

  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  # reverse list form mid+1

  midHead = Rev_list(slow.next)
  start = head
  end =  midHead

  while end is not None:
    if start.data != end.data:
      Rev_list(midHead)
      return False

    start= start.next
    end = end.next

  Rev_list(midHead)
  return True
####################################################################

    
###########################################
#########################
# Driver code
if __name__ == "__main__":
  arr = [1, 2, 12, 1]
  head = Node(arr[0])
  head.next = Node(arr[1])
  head.next.next = Node(arr[2])
  head.next.next.next = Node(arr[3])
  head = Palindrome_hash_2_PO(head)
  print(head)
