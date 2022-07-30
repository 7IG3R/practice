# You are given an integer array A of length N, where O <= A[i] <= N for each index i.
# The following operation can be performed on A:
# Increase the value of any element of A by 1.
# 
# A number k is called beautiful if the MEX of A becomes k after performing the
# operation any number of times.
# 
# Let there be an array B containing all possible beautiful numbers that can be
# obtained from A using the given operation.
# Your task is to return B after sorting it in ascending order.
# 
# The MEX of A is equal to the minimum non-negative integer that is NOT in A
# 
# Input Format
# The first line contains an integer. N, denoting the number of elements in A
# Eack line i of the N subsequent lines (where O <= i < N) contains an integer describing A[i]
# 3      0
# 0      1
# 2
# 2
# index 0 to to +1 then MEX is 0 and if left this way only then MEX is 1 so ans is 0,1

