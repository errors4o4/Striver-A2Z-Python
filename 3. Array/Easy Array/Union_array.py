arr1 = [1, 1,2,3,4,6,7,]
arr2 = [2, 3, 4, 4, 5]
union = []

i = 0
j = 0

while (i < len(arr1) and j < len(arr2)):
  #  ele of arr1 is smaller than ele of arr2
  # if union len is 0 or ele of arr1 is not equal to last ele of union
  # append ele of arr1 in the union and increment i 
  if (arr1[i] <= arr2[j]):
    if (len(union) == 0 or arr1[i] != union[-1]):
      union.append(arr1[i])
    i += 1

  # if union len is 0 or ele of arr2 is not equal to last ele of union
  # append ele of arr2 in the union and increment j
  else:
    if (arr2[j] != union[-1] or len(union) == 0):
      union.append(arr2[j])
    j += 1

# if 2nd arr is exausted then check ele in arr1 is not eqaul to last ele of union 
#append arr1 ele and increment i 
while (i <= len(arr1) - 1):
  if (arr1[i] != union[-1] or len(union) == 0):
    union.append(arr1[i])
  i += 1

# if 1nd arr is exausted then check ele in arr2 is not eqaul to last ele of union 
#append arr2 ele and increment j
while (j <= len(arr2) - 1):
  if (arr2[j] != union[-1] or len(union) == 0):
    union.append(arr2[j])
  j += 1

print(union)
