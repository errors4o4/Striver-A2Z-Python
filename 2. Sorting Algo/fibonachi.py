n = 5

def fibonachi(i):
  if (i<=1):
    return i

  last = fibonachi(i - 1)
  secondLast = fibonachi(i - 2)
  return last + secondLast

print(fibonachi(6))
