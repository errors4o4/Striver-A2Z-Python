a = [60, 50,45, 40,98, 30, 20, 9]

for i in range(len(a)):
  j = i
  while (j>0 and a[j-1]>a[j]):
    a[j-1],a[j] = a[j],a[j-1]
    j-=1
print(a)

def RISort(arr, rang):
  j = rang
  while(j>0 and arr[j-1]>a[j]):
    arr[j-1],a[j] = arr[j],a[j-1]
    j-=1
  