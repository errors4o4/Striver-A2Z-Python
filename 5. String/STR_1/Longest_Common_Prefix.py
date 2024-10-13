str = ["flower", "flows", "flight"]


def longestCommonPrefix(str):
  ans = ''
  str = sorted(str)
  first = str[0]
  last = str[-1]
  
  for i in range(min(len(first), len(last))):
    if (first[i] != last[i]):
      return ans
    ans += first[i]

  return ans


print(longestCommonPrefix(str))
