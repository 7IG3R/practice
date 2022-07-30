# You are given an array A of size N
# You can perform the following operations on A:
# • Pick any two indices i and j in A such that i != j
# • Divide A[i] and A[j] by some common factor of A[i] & A[j]

# Find the minimum possible product of the elements of A after performing the
# given operations as many times as required. Since the answer can be very
# large return it modulo 10^9+7

# Input Format
# The first line contains an integer, N denoting the number of elements in A
# Each line i of the N subsequent lines (where 0 <= i < N) describes A[i]

# 2          7
# 7
# 49

# Here N=2 A=[7,49] We
# can select (7,49) and
# divide both by 7 then A
# becomes [1,7] with
# product 7

# 3       1
# 2
# 3
# 6
