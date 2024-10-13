nums = [4, 2, 2, 6, 4]
k = 6

def count_sub(nums, k):
  xr = 0
  mpp = {}
  mpp[xr] = 1  # {0 : 1}
  count = 0

  for i in range(len(nums)):
    xr = xr ^ nums[i]

    x = xr ^ k

    count += mpp.get(x, 0)

    mpp[xr] = mpp[xr] + 1
  return count


# def count_sub(nums, k):
#   count = 0
  
#   for i in range(len(nums)):
#     xor = 0
#     for j in range(i, len(nums)):
#       xor = xor ^ nums[j]
  
#       if (xor == k):
#         count += 1
  
#   return count

print(count_sub(nums, k))
