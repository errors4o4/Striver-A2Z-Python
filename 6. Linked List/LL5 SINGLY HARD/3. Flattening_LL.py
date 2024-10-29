##############################################################
#BRUTE 
def flatten(self, root):
  ans = []
  temp = head

  while temp != None:
    t2= temp
    while t2 != None:
      ans.append(t2.data)
      t2 = t2.bottom
    temp = temp.next

  ans.sort()
  firstNode = Node(ans[0])
  t1 = firstNode

  for i in range(1, len(ans)):
    newNode = Node(ans[i])
    t1.bottom = newNode
    t1 = newNode

  return firstNode

##############################################################
#OPTIMAL

def merge2LL(L1, L2):
  dummyNode = Node(-1)
  res = dummyNode

  while L1 != None and L2 != None:
    if L1.data < L2.data:
      res.bottom = L1
      res = L1
      L1 = L1.bottom

    else:
      res.bottom = L2
      res = L2
      L2 = L2.bottom
      
    res.next = None

  if L1 != None:
    res.bottom = L1
  elif L2 != None:
    res.bottom = L2

  return dummyNode.bottom


def flatten(self, root):
  if head == None or head.next == None:
    return head

  mergedHead = self.findLast(head.next)

  return merge2LL(head, mergedHead)