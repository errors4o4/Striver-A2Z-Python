arr = [10, 10, 70, 20, 50, 30, 60]
# arr = [10, 20, 30, 40, 50, 60]


def isArraySort(arr):
  for i in range(len(arr) - 1):
    print(arr[i])
    if (arr[i] > arr[i + 1]):
      return False
  return True


print(isArraySort(arr))
