nums = [1, -1, 3, 2, -2, -8, 1, 7, 10, 12]

def long_sub(nums):
  maxi = 0
  mpp = {}
  sum = 0

  for i in range(len(nums)):
    sum += nums[i]

    if sum == 0:
      maxi = i + 1

    else:
      if (sum in mpp):
        maxi = max(maxi, i-mpp[sum])

      else:
        mpp[sum] = i
  
  return print(maxi)

long_sub(nums)
