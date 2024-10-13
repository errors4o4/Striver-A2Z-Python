nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 5

# def sum_list(nums):
#   max_wight = 0

#   for i in range(len(nums)):
#     max_wight += nums[i]

#   return max_wight

def days_req(nums, cap):
  days = 1
  load = 0

  for i in range(len(nums)):
    if(load + nums[i]) > cap:
      days += 1
      load = nums[i]

    else: 
      load += nums[i]

  return days
      

def ship_cap(nums, d):
  low = max(nums)
  high = sum(nums)

  while(low<=high):
    mid = (low + high)//2

    no_of_days = days_req(nums, mid)
    print(no_of_days)

    if (no_of_days <= d):
      high = mid -1

    else:
      low = mid +1

  return low

    
print(ship_cap(nums, d))

