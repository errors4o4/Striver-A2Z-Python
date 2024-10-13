s = "anagram"
t = "anagrsm"


def isAnagram(s, t):
  if len(s) != len(t):
    return False

  freq = {}

  for i in range(len(s)):
    freq[s[i]] = freq.get(s[i], 0) + 1

  for i in range(len(t)):
    freq[t[i]] = freq.get(t[i], 0) - 1

  for value in freq.values():
    if value != 0:
        return False

  return True


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True

print(isAnagram(s, t))
