nums = [  # m j
    [1, 1, 1, 1],  #n i
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]


def setZeroes(nums):
  # Get the number of rows (n) and columns (m) in the matrix
  n = len(nums)
  m = len(nums[0])

  # Initialize a flag to track if the first column should be set to zero
  col0 = 1

  # First pass: mark rows and columns that need to be set to zero
  for i in range(n):
    for j in range(m):
      if nums[i][j] == 0:
        # Mark the first element of the row as zero
        nums[i][0] = 0
        # Mark the first element of the column as zero if it's not in the first column
        if j != 0:
          nums[0][j] = 0
        else:
          # If the zero is in the first column, set the flag to zero
          col0 = 0

  # Second pass: set elements to zero based on markers in the first row and column
  for i in range(1, n):
    for j in range(1, m):
      if nums[i][j] != 0 and (nums[i][0] == 0 or nums[0][j] == 0):
        # If the current element is not zero, check markers to determine if it should be set to zero
        nums[i][j] = 0

  # Handle the first row separately if it contains a zero marker
  if nums[0][0] == 0:
    for j in range(m):
      nums[0][j] = 0

  # Handle the first column separately if the flag is set
  if col0 == 0:
    for i in range(n):
      nums[i][0] = 0

  # Return the modified matrix
  return nums


setZeroes(nums)
# print(nums)
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
