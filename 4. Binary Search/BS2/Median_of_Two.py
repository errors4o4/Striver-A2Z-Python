def median(a, b):
  n1, n2 = len(a), len(b)
  i, j = 0, 0
  n = (n1 + n2)
  ind2 = n / 2
  ind1 = ind2 - 1
  cnt = 0
  ind1el = -1
  ind2el = -1

  while (i < n1 and j < n2):

    if (a[i] < b[j]):
      if (cnt == ind1):
        ind1el = a[i]
      if (cnt == ind2):
        ind2el = a[i]
      cnt += 1
      i += 1

    else:
      if (cnt == ind1):
        ind1el = b[j]
      if (cnt == ind2):
        ind2el = b[j]
      cnt += 1
      j += 1

  while (i < n1):
    if (cnt == ind1):
      ind1el = a[i]
    if (cnt == ind2):
      ind2el = a[i]
    cnt += 1
    i += 1

  while (j < n2):
    if (cnt == ind1):
      ind1el = b[j]
    if (cnt == ind2):
      ind2el = b[j]
    cnt += 1
    j += 1

  if (n % 2 == 1):
    return ind2el

  return (ind1el + ind2el) // 2
