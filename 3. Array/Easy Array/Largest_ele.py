arr = [10, 70, 20, 50, 30, 60]


def largest(arr):
  if (len(arr) <= 1):
    return print(arr[0])

  lar = arr[0]
  for i in range(len(arr) - 1):
    if (arr[i] > lar):
      lar = arr[i]
  print(lar)


largest(arr)
