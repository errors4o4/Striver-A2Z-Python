n = 5
arr = 'ABasdCDCBA'

def reversed(l,r):
  if (l>=r):
    return
  if (arr[l] != arr[r]):
    print("String is not palindrome")
    return
  print("String is palindrome")
  reversed(l+1, r-1)

reversed(0,len(arr)-1)  