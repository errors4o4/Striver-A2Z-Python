a = [60, 50,45, 40,98, 30, 20, 9]


def Rbubble_sort(arr, right):
  left = 0
  # right = len(arr) -1 
  while(left<right):
    if (arr[left] >= arr[left+1]):
      arr[left],arr[left+1] = arr[left+1],arr[left]
    left +=1


def RBsort(arr):
  right = len(arr) -1 

  while(0<right):
    Rbubble_sort(arr, right)
    right -= 1

RBsort(a)
print(a)

  


