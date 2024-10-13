arr =[1,2,3,4,5,6,7]

print(arr)


def leftRotate(arr, d):
  d = d%len(arr)    # rotate 12 means 5+5+2 skip 5+5 and rotate 2 times
  temp = arr[:d]     # storing first D values in temp
  print(temp)

  for i in range(d, len(arr) ):    # rotate from d to end of array
    arr[i - d] = arr[i]    # start from d = 2 till end. so 2-2, 3-2 ....

  for j in range(len(arr)-d, len(arr)):   # placing temp at the end 
    arr[j] = temp[j-(len(arr)-d)]      # start from len(arr)-d = 3 to end 
  #placing temps val (3-(5-2)) to the d+1 place of array
  
  return print(arr)


leftRotate(arr, 2)
