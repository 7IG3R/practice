# D
# You are given two array A & B of size N
# The following operation can be performed on A:
# Choose at-most 2 indexes i and j from A such that Ai + Aj <= K.
# It is also given that for selected index i you obtain a profit Bi
# Find the maximum profit that can be obtained
# The given array follow 0 based indexing.

# Input Format
# The first line contains an integer, N, denoting the number of elements in A.
# The next line contains an integer, K, denoting the value of K described in the problem.
# Each line i of the N subsequent lines (where 0 <= i < N) contains an integer describing A[i]
# Each line i of N subsequent lines (where 0 <= i < N) contains an integer describing B[i]
# 2         2
# 2
# 1
# 2
# 2
# 1
# Here N=2 K=2, we can select 0th index and get a profit 2

# 4       7
# 7
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# Here N=4 K=7 We can select 3rd & 2nd index, given 0 based index, we will get a profit of 4+3=7
# 
