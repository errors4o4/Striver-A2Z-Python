arr = [1, 2, 4]


def findMiss(arr):
  n = len(arr) +1
  sum1 = 0
  for i in range(len(arr)):
    sum1 += arr[i]

  sum2 = (n * (n + 1)) // 2
  return print(sum2 - sum1)

  # hash = [0]* (n+1)
  # if len(arr)<n:
  #   for i in range(len(arr)):
  #     hash[arr[i]] = 1

  #   for j in range(1, len(hash)):
  #     if hash[j] == 0:
  #       return print(j)


findMiss(arr)
