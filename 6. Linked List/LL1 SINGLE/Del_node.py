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


##############################################
########## DELETE 1ST NODE
def Del_head(head):
  if head == None:
    return head

  temp = head.next
  head = temp
  return head


###############################################


###############################################
########## DELETE LAST NODE
def Del_tail(head):
  if head == None or head.next == None:
    return head

  temp = head
  while temp.next.next is not None:
    temp = temp.next

  temp.next = None
  return head


###############################################


###############################################
########## DELETE PARTICULAR NODE
def Del_pos(head, pos):
  pos -= 1
  temp = head.next
  count = 1
  prev = None

  if head == None or head.next == None:
    return head

  if pos == 1:
    temp = Del_head(head)
    return temp

  for i in range(1, pos):
    prev = temp
    temp = temp.next

    if temp is None:
      return head

  if temp is not None:
    prev.next = temp.next

  return head
###############################################


###############################################
########## DELETE PARTICULAR NODE
# !. check if its 1st ele then delete 
# 2. else fine the ele change pre.next = prev.next.next
def Del_val(head, val):
  

  if head == None :
    return head

  if head.data == val:
    temp = head 
    head = head.next
    return head

  temp = head
  prev = None

  while temp is not None:
    if temp.data == val:
      prev.next = prev.next.next
    
    prev = temp
    temp = temp.next


  return head


###############################################

if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  head = arr2List(arr, n)
  # head = Del_head(head)
  # head = Del_tail(head)
  # head = Del_pos(head, 3)
  head = Del_val(head, 2)
  display(head)
