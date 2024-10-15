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
    temp = Node(arr[i], None, prev)
    prev.next = temp
    prev = temp
  return head


def display(head):
  temp = head
  while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next


#######################################
# INSERT HEAD
def Ins_head(head, val):
  if head is None:
    return head

  # newNode = Node(val, head)
  newNode = Node(val)
  newNode.next = head
  head.back = newNode

  return newNode


#######################################


#######################################
# INSET END OF LIST
def Ins_end(head, data):
  new = Node(data)
  if head is None:
    head = new
    return head

  temp = head
  while temp.next is not None:
    temp = temp.next

  temp.next = new
  new.back = temp

  return head


#######################################


#######################################
# INSERT BEFORE END
def Ins_bef_End(head, val):
  if head is None:
    return head

  if head.next is None:
    newNode = Node(val, head)
    head.back = newNode
    return newNode

  temp = head
  while temp.next is not None:
    temp = temp.next

  # prev = temp.back
  # newNode = Node(val, temp, prev)
  # prev.next = newNode
  # temp.back = newNode

  newNode = Node(val)
  prev = temp.back
  newNode.back = temp.back
  newNode.next = temp
  temp.back = newNode
  prev.next = newNode

  return head
#######################################

#######################################
# INSERT BEFORE POSITION
def Inser_bef_Pos(head, val, pos):
  if head is None:
    return head

  if pos == 1:
    newNode = Node(val, head)
    head.back = newNode
    return newNode

  temp = head
  count = 0
  prev = None

  while temp.next is not None:
    count += 1
    if pos == count:
      break
    temp = temp.next
    
  # prev = temp.back
  # newNode = Node(val, temp, prev)
  # prev.next = newNode
  # temp.back = newNode

  prev = temp.back
  newNode = Node(val)
  newNode.next = temp
  newNode.back = prev
  prev.next = newNode
  temp.back = newNode
  
  return head 
#######################################

#######################################
# INSERT BEFORE posValue
def Ins_bef_val(head, val, posValue):
  if head is None:
    return head

  temp = head
  prev = None
  while temp.next is not None:
    if temp.data == posValue:
      break
    temp=temp.next

  prev = temp.back
  newNode = Node(val, temp, prev)
  temp.back = newNode
  prev.next = newNode

  # prev = temp.back
  # newNode = Node(val)
  # newNode.next = temp
  # newNode.back = temp
  # temp.back = newNode
  # prev.next = newNode

  return head
#######################################

# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  # head = Ins_end(head, 6)
  head = Ins_bef_val(head, 10, 4)
  display(head)
