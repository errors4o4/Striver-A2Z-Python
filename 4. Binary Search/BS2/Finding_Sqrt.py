n = 38


def bs2(n):
  low = 0
  high = n

  while(low<=high):
    mid = (low+high)//2

    if(mid*mid) <= n:
      low = mid +1

    else:
      high= mid-1
  return high


print(bs2(n))