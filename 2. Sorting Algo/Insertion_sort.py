a = [20, 13, 46, 24, 52, 9]

for i in range(len(a)):
  j = i
  while (j>0 and a[j-1]>a[j]):
    a[j-1],a[j] = a[j],a[j-1]
    j-=1
print(a)