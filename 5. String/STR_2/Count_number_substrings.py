s = "aabcbaa"
k = 7


def beautySum(s, k):
  n = len(s)
  mpp = {}
  maxlen = 0
  L = 0
  r = 0

  while ( r < n):
    mpp[s[r]] = mpp.get(s[r], 0) + 1

    if (k < len(mpp)):  
      mpp[s[L]] =  mpp[s[L]] - 1
      if (mpp[s[L]]) == 0:
        mpp.pop(s[L])
      L += 1

    if (k >= len(mpp)):
      maxlen = max(maxlen, r-L+1)
      r += 1
  
  return maxlen


print(beautySum(s, k))