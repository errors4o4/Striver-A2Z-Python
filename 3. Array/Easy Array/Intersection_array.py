arr1 = [1, 1, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]
intersection = []
i, j = 0, 0
k = 0

while(i<len(arr1) and j<len(arr2)):
  if (arr1[i] < arr2[j]):
    i += 1
  elif (arr1[i] > arr2[j]):
    j += 1
  else:
    intersection.append(arr1[i])
    i += 1
    j += 1
    

print(intersection)
