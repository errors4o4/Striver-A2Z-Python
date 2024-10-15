class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


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
# INSERT AT START
def ins_head(head, newNode):
  new = Node(newNode)
  new.next = head
  return new


#######################################


#######################################
# INSERT AT END
def ins_tail(head, newNode):
  new = Node(newNode)

  if head is None:
    head = new
    return head

  temp = head
  while temp.next is not None:
    temp = temp.next

  temp.next = new
  return head


#######################################
# INSERT AT POS
def ins_pos(head, newNode, pos):
  new = Node(newNode)

  if head is None:
    if pos == 1:
      return new
    else:
      return None

  if pos == 1:
    new.next = head
    return new

  temp = head
  count = 0
  while temp.next is not None:
    count += 1
    
    if count == pos-1:
      new.next = temp.next
      temp.next = new
      return head
      
    temp = temp.next

  if temp.next is None:
    temp.next = new
    return head
  

#######################################

#######################################
# INSERT BEFORE VALUE
def ins_val(head, newNode, val):
  new = Node(newNode)

  if head is None:
    return new

  temp=head
  prev = None

  while temp.next is not None:
    if temp.data == val:
      new.next = temp 
      prev.next =  new
      
    prev = temp
    temp =  temp.next

#######################################

if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  head = arr2List(arr, n)
  # head = ins_head(head, 0)
  # head = ins_tail(head, 6)
  head = ins_pos(head, 8, 9)
  display(head)
