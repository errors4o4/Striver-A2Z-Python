a = [20, 13, 46, 24, 52, 9]

for i in reversed(range(len(a) )):
  for j in range(0,i):
    if (a[j]>a[j+1]):
      a[j],a[j+1] = a[j+1],a[j]
print(a)


