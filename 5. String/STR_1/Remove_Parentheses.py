s = '(()())(())(()(()))'

def removeOuterParentheses(s):
  result = []
  opened = 0

  for char in s:
    if char == '(' :
      if opened > 0:
        result.append(char)
      opened +=1

    elif char == ')':
      if opened > 1:
       result.append(char)
      opened -=1

  return ''.join(result)


print(removeOuterParentheses(s))
