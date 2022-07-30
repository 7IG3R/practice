# 2-1 - 2-4
# You are given an array A of N integer, and two integers X and Y
# You need to make all elements of the array equal by performing the following operation any number of times:
# 1. Pick an index i where (O <= i < N).
# 2. Perform any one of the following:
# Increase Ai by X.
# Increase Ai by Y
# Decrease Ai by X.
# Decrease Ai by Y. 

# If it is possible to make all the elements of the array equal, let B denote an array with all
# elements equal to the smallest non-negative number each element can be made equal
# to. Otherwise, array B is an array of size N, with each element equal to -1.
# Find Array B

# Input Format
# The first line contains an integer, N, denoting the number of elements in A.
# The next line contains an integer, X, denoting the number which you can add/subtract.
# The next line contains an integer, Y, denoting the number which you can add/subtract.
# Each line i of the N subsequent lines (where 0 si < N) contains an integer describing A[i]
# 5     0
# 3     0
# 2     0
# 1     0
# 4     0
# 5
# 6
# 7
# We can do the operations
# in following order: 
# 1. Increase A[0] by 2. 
# 2. Decrease A[0] by 3. 
# 3. Decrease A[1] by 2. 
# 4. Decrease A[1] by 2. 
# 5. Decrease A[2] by 2. 
# 6. Decrease A[2] by 3. 
# 7. Decrease A[3] by 3. 
# 8. Decrease A[3] by 3. 
# 9. Decrease A[4] by 2. 
# 10. Decrease A[4] by 2. 
# 11. Decrease A[4] by 3.