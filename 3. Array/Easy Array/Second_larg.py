arr = [10, 70, 20, 50, 30, 60]


def largest(arr):
  if (len(arr) <= 1):
    return print(arr[0])

  slar = -1
  lar = arr[0]
  for i in range(len(arr) ):
    if (arr[i] > lar):
      slar = lar
      lar = arr[i]
    elif (arr[i]<lar and arr[i]>slar):
      slar = arr[i]
  print(slar)


largest(arr)
