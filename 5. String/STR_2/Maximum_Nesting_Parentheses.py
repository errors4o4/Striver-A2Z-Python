s = "1+(2*3)/(2-1)"


def maxDepth(s):
  maxDepth = 0
  stack = []
  for char in s:
      if char == '(':
          stack.append(char)
      elif char == ')':
          stack.pop()

      maxDepth = max(maxDepth, len(stack))

  return maxDepth
    

print(maxDepth(s))