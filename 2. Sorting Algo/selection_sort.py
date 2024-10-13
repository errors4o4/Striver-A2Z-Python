a= [20,13, 46, 24, 52, 20, 9]

for i in range(len(a)-1):
  min = i
  for j in range(i,len(a)):
    if (a[j] < a[min]):
      min = j
      a[i], a[min] = a[min], a[i]

print(a)