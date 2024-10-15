class Node:

  def __init__(self, data, next=None, back=None):
    self.data = data
    self.next = next
    self.back = back


# Insert !st ele of arr i list and store prev = head for future
# loop through arr from 1 to n.
# 1. insert new ele and set back = prev
# 2. set prev.next = temp (connet back and current ele)
# 3, set prev=temp for future
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
    temp = temp

  #######################################
  # WRITE CODE

  #######################################

  # Driver code
  if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = array_to_list(arr)
    display(head)
