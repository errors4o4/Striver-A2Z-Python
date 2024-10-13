nums = [1, 2, 3, 1, 1, -1, 1, 1, 3, 3]
k = 6


def long_com(k, nums):
  n = len(nums)
  sum = 0
  maxlen = 0
  hashset = {}

  for i in range(n):
    sum += nums[i]

    if sum == k:
      maxlen = max(maxlen, i + 1)

    rem = sum - k

    if rem in hashset:
      lenn = i - hashset[rem]
      maxlen = max(maxlen, lenn)

    if sum not in hashset:
      hashset[sum] = i

  return maxlen


print(long_com(k, nums))

nums = [1, 2, 3, 1, 1, 1, 1, 3, 3]


def long_com(k, nums):
  left = 0
  right = 0
  sum = nums[0]
  maxlen = 0

  while (right < len(nums)):

    while (left <= right and sum > k):
      sum -= nums[left]
      left += 1

    if (sum == k):
      maxlen = max(right - left + 1, maxlen)

    right += 1
    if (right < len(nums)):
      sum += nums[right]

  return print(maxlen)


long_com(k, nums)
