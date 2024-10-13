num = "4206"


def largestOddNumber(num):
  n = len(num)

  for i in reversed(range(n)):
    if (int(num[i]) % 2 != 0):
      return num[:i + 1]

  return ""


print(largestOddNumber(num))
