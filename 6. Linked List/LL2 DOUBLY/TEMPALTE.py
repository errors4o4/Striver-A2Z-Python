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
    temp = Node(arr[i], None,prev)
    prev.next = temp
    prev = temp
  return head


def display(head):
  temp = head
  while temp is not None:
    print(temp.data, end=" ")
    temp =temp.next


  #######################################
  # WRITE CODE

  #######################################

  # Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  display(head)
