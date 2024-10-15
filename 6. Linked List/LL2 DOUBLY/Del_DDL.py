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
# DEl head
def Del_head(head):
  if head is None:
    return head

  if head.next is None:
    head = None
    return head

  front = head.next
  head.next = None
  front.back = None

  return front


#######################################


#######################################
# DEl end
def Del_end(head):
  if head is None:
    return head

  temp = head
  while temp.next is not None:
    temp = temp.next

  prev = temp.back
  prev.next = None
  temp.back = None

  return head


#######################################


#######################################
# DEl end
def Del_pos(head, pos):
  if head is None:
    return head

  temp = head
  count = 0
  while temp is not None:
    count += 1
    if count == pos:
      break
    temp = temp.next

  prev = temp.back
  front = temp.next

  if (prev == None and front == None):
    temp = None
    return head

  elif (prev == None):
    temp.next = None
    front.back = None
    return front

  elif (front == None):
    prev.next = None
    temp.back = None
    return head

  prev.next = front
  front.back = prev
  temp.next = None
  temp.back = None

  return head
######################################


######################################
# DELETE VALUE
def Del_val(head, val):
  if head is None:
    return head

  temp = head
  while temp.next is not None:
    if temp.data == val:
      break

    temp = temp.next

  prev = temp.back
  front = temp.next

  if front == None:
    prev.next = None
    temp.back = None

  else:
    prev.next = front
    front.back = prev
    temp.next = None
    temp.back = None

  return head
######################################


# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  # head = Del_end(head)
  # head = Del_pos(head, 1)
  head = Del_val(head, 2)
  display(head)
