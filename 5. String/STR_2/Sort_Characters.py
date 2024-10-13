s = "raaeaedere"
# s = "bbAa"


def frequencySort(s):
  mpp = {}
  n = len(s)
  ans = ''
  
  for i in range(n):
    mpp[s[i]] = mpp.get(s[i], 0) + 1

  for val in reversed(mpp):
    
    while(mpp[val] > 0):
      ans+= val
      mpp[val] -= 1
      

  return ans
  

print(frequencySort(s))
