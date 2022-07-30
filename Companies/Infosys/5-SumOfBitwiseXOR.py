# You are given an array A of N Positive number
# Let's define a multiset S as the collection of max(Ai, Ai+1, ..., Ar) for every 1 <= i <= r <= N.
# Formally, it is the collection of the maximum value of every non empty subarray of A.
# Find the sum of bitwise XOR (Exclusive OR) of every pair x, y where x, y E S. Since the
# answer can be large, Jeturn it modulo 10^9+7
# The given array A is 1-indexed.

# Input Format
# The first line contains an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 1 <= i <= N) contains an integer describing A[i].
# 2     6
# 1
# 2

# Given array is [1, 2].
# max({A[1]}) = 1
# max({A[2]} ) = 2 
# max({A[1], A[2]}) = 2 Thus, answer is
# (1 ^ 2) + (1 ^ 2) + (2 ^ 2) = 3 + 3 + 0 = 6.