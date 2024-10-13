# s = "babad"
s = 'sggasaggs'


def longestPalindrome(s):
  n = len(s)
  res = ''
  reslen = 0

  for i in range(n):

    # odd length
    l = i
    r = i
    while (0 <= l and r < n and s[l] == s[r]):
      if (r - l + 1) > reslen:
        res = s[l:r + 1]
        reslen = r - l + 1
      l -= 1
      r += 1

    # even condition
    l = i
    r = i + 1
    while (0 <= l and r < n and s[l] == s[r]):
      if (r - l + 1) > reslen:
        res = s[l:r + 1]
        reslen = r - l + 1
      l -= 1
      r += 1

    return res
    


print(longestPalindrome(s))
