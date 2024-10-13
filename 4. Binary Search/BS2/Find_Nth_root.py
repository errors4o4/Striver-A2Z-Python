N = 3
M = 27

# return 1 if ans == m
# return 0 if ans < m
# return 2 if ans > m


def mul(mid, N, M):
  ans = 1
  for i in range(1, N + 1):
    ans *= mid

    if (ans > M):
      return 2

    if (ans == M):
      return 1

  return 0


def bs2(N, M):
  low = 1
  high = M

  while (low <= high):
    mid = (low + high) // 2
    midN = mul(mid, N, M)
    
    if (midN == 1):
      return mid

    elif (midN < 0):
      low = mid + 1

    else:
      high = mid - 1

  return -1


print(bs2(N, M))
