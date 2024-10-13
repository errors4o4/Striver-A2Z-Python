arr = [10,10,10, 20, 30, 40, 50, 50, 60, 60, 60]

print(arr)

def removeDup(arr):
  i=1
  while(i<len(arr)):
    if (arr[i] == arr[i-1]):
      arr.remove(arr[i])
      i -= 1  
    i += 1  
  return print(arr)
removeDup(arr)

# # # # # # # # # # OPTIMAL
arr=[1,1,2,2,2,3,3]
def removeDupOP(arr):
  uniq = 0

  i = 1
  while(i<len(arr)):
    if(arr[uniq] != arr[i]):
      uniq +=1 
      arr[uniq], arr[i] = arr[i], arr[uniq]
    i += 1

  return print(arr[:uniq +1 ])    

removeDupOP(arr)