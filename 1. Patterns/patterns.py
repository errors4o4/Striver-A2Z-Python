# 1
# a, b = map(int, input().split())

# for i in range(0, a):
#   for j in range(0, b):
#     print('*', end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 2
# for i in range(0, a):
#   for j in range(0, b):
#     if (i >= j):
#       print('*', end='')
#     else:
#       break
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 3
# for i in range(1, a):
#   for j in range(1, b):
#     if (i >= j):
#       print(j, end='')
#     else:
#       break
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# for i in range(1, a):
#   for j in range(1, b):
#     if (i >= j):
#       print(i, end=' ')
#     else:
#       break
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 4
# for i in range(a+1):
#   for j in range(1, (a-i)):
#     print(j, end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 7
# a=9

# for i in range(a+1):
#   for j in range( (a-i-1)):
#     print(' ', end='')
#   for k in range( (2*i+1)):
#     print('*', end='')
#   for l in range( (a-i-1)):
#       print(' ',end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 8
# a=5

# for i in range(a):
#   for j in range( (i)):
#     print(' ', end='')
#   for k in range( (2*a-2*i-1)):
#     print("*", end='')
#   for l in range( (i)):
#       print(' ',end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 10
# a=5

# for i in range(a+1):
#   for j in range( i):
#     print('*', end='')
#   print('\n')

# for i in range(a+1):
#   for j in range( a-i):
#     print('*', end='')
#   print('\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 9
# a=5

# for i in range(a):
#   for j in range( (a-i-1)):
#     print(' ', end='')
#   for k in range( (2*i+1)):
#     print('*', end='')
#   for l in range( (a-i-1)):
#       print(' ',end='')
#   print('\n')

# for i in range(a):
#   for j in range( (i)):
#     print(' ', end='')
#   for k in range( (2*a-2*i-1)):
#     print("*", end='')
#   for l in range( (i)):
#       print(' ',end='')
#   print('\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 11
# a=5

# for i in range(a+1):
#   for j in range( i):
#     if( i%2==0):
#       if( j%2==0):
#         print('1', end='')
#       else:
#         print('0', end='')
#     else:
#       if( j%2==0):
#         print('0', end='')
#       else:
#         print('1', end='')

#   print('\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 12
# a=5
# for i in range(a+1):
#   for j in range(i):
#     print(j+1, end='')
#   for k in range(2*a-2*i):
#     print(" ", end='')
#   for l in reversed(range(i)):
#     print(l+1, end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 13
# a=5
# b =1
# for i in range(a+1):
#   for j in range(i):
#     print(i+j, end='')
#   print('\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# 14
# import string

# alpha = string.ascii_uppercase
# a = 5

# for i in range(a+1):
#   for j in range(i):
#     print(alpha[j], end='')
#   print('\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 15
# import string

# alpha = string.ascii_uppercase
# a = 5

# for i in range( a + 1):
#   for j in range(i):
#     print(alpha[i], end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 17
# import string

# alpha = string.ascii_uppercase
# a = 5

# for i in range( a + 1):
#   for j in range(a-i):
#     print(' ', end='')
#   for k in range(i):
#     print(alpha[k], end='')
#   for l in reversed(range(i-1)):
#     print(alpha[l], end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # 18
# import string

# alpha = string.ascii_uppercase
# a = 5

# for i in range( a+1 ):
#   for j in reversed(range(i)):
#     print(alpha[a-j-1], end='')
#   print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # 19
# a = 5

# for i in range(a ):
#   for j in range(a - i):
#     print("*", end='')
#   for k in range(2 * i):
#     print(" ", end='')
#   for j in range( a - i):
#     print("*", end='')
#   print()

# for i in range( a ):
#   for j in range(i+1):
#     print("*", end='')
#   for k in range(2 * (a - i-1)):
#     print(" ", end='')
#   for j in range( i+1):
#     print("*", end='')
#   print()

# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 20
# a = 5

# for i in range(a+1 ):
#   for j in range(i):
#     print("*", end='')
#   for k in range(2*(a-i)):
#     print(" ", end='')
#   for j in range( i):
#     print("*", end='')
#   print()

# for i in range(a):
#   for j in range(a-i):
#     print("*", end='')
#   for k in range(2*(i)):
#     print(" ", end='')
#   for j in reversed(range( a-i)):
#     print("*", end='')
#   print()
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 21
# a = 5
# for i in range(a):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a - 1 or j == a - 1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# 22
a = 6
for i in range(a):
    for j in range(a):
        if i == 0 or j == 0 or i == a - 1 or j == a - 1:
            print(a - 1, end=' ')
        else:
            print(a - i, end=' ')
    print()
