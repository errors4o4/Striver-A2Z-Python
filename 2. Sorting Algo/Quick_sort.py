a = [60, 50,45, 40,98, 30, 20, 9]


for i in range(len(a)-1):
  j = len(a) -1 

  if (a[i] > a[i+1]):
    a[i], a[i+1] = a[i+1], a[1]
  print(a[i])
