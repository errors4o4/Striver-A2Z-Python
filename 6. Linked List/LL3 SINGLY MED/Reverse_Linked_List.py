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
# NORMAL METHOD
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
#############################################################

#############################################################
# Recursive  METHOD
def Rev_list_ruc(head):
  if head == None or head.next == None:
    return head

  newHead = Rev_list_ruc(head.next)
  front = head.next
  front.next =head
  head.next = None

  return newHead
#############################################################
# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  # head = Find_Middle(head)
  head = Rev_list_ruc(head)
  display(head)
