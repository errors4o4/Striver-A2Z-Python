# INTRODUCTION
class Node:

  def __init__(self, data1, next1=None):
    self.data = data1
    self.next = next1


# Creating a new Node with the value from the array
y = Node(2)
# Printing the data stored in the Node
print(y)

#####################################################


# FIRST POINT TO THE NEXT ONE
# X is 1st ine and Y pointing to the X
class Node:

  def __init__(self, data1, next1=None):
    self.data = data1
    self.next = next1


# Creating a Node 'x' with the first element of the array
x = Node(2)
# Creating a reference 'y' pointing to the same Node 'x'
y = x
# Printing the reference 'y', which represents the memory address of the Node 'x'
print(y)

############################################################

# ARRAY TO LINKEDLIST
#1st METHOD


# INSERT ELE IN LIST
# 1. create new node
# 2. check the node is none: return temp #temp means new head # menas its empty list
# 3. set last = head # head means 1st ele
# 4. check until find the last ele # if its last ele then it dont point to the next ele
# 5. after finding the last ele then it point to the them # temp in newly inserted ele
# 6. return head ele # which is 1st ele
def insert_end(head, item):
  temp = Node(item)
  if head is None:
    return temp  # temp means new head

  last = head
  while last.next is not None:
    last = last.next

  last.next = temp
  return head


# 1. set head to None for 1st ele in list
# 2. loop list item
# 3. call insert_end func and pass (head, item) # if head-> null then it will create new LL and append the ele
# 4. retrun the head # 1st ele in the list.
def array_to_list(arr):
  head = None
  for item in arr:
    head = insert_end(head, item)
  return head


# NEVER tamper head
# store head in temp
# loop until find last node
# print temp.data
# assign the temp = next node's pointer
def display(head):
  temp = head
  while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next


# Driver code
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  head = array_to_list(arr)
  display(head)


######################
#2nd METHOD
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


def display(head):
  temp = head

  while (temp != None):
    print(temp.data, end=' ')
    temp = temp.next


def arr2List(arr, n):
  head = None
  for i in range(n - 1, -1, -1):
    head = insert(head, arr[i])
  return head


if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  head = arr2List(arr, n)
  display(head)
