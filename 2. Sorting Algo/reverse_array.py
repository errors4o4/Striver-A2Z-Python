n = 5

arr = [5,4,3,2,1]

def reversed(l,r):
  if (l>=r):
    print(arr)
    return
  arr[l], arr[r] = arr[r], arr[l]
  reversed(l+1, r-1)

reversed(0,len(arr)-1)