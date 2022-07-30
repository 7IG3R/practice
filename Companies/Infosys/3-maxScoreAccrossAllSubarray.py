# D
# You are given an array A of length N, on which the following operations can be done:
# Select an index i and make A[i] = -A[i]

# The score of subarray is defined as the absolute value of the sum of all the elements
# in that sub array

# you are allowed to perform atmost M operations on A
# Find the maximum value of score across all possible subarrays of A with length K.

# Input Format
# The first line contains an integer, N, denoting the number of elements in A.
# The next line contains an integer, M, denoting the maximum number of operations you can perform.
# The next line contains an integer, K, denoting the value K described in the problem.
# Each line i of the N subsequent lines (where 0 <= i < N) contains a long describing A[i].
# 3    1
# 1
# 1
# 1
# -1
# 1
# Here N=3, M=1 Without doing any operation we will have 
# max score of 1 as (0,0) subarray has value 1 and is of length 1

# 3    4
# 1
# 2
# -3
# 1
# -2
# N = 3 M = 1 K = 2
# On 0th index A = [3,1,-2] so 0+1 = 3+1 = 4
