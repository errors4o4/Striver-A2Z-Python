arr = [1,2,3,4,5]

def leftRotate(arr):
  for i in range(len(arr)-1):
    arr[i], arr[i+1] = arr[i+1], arr[i]  
  return print(arr)

leftRotate(arr)