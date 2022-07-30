# you will be given N cubes. It is given that ith cube has value A[i] which
# describes It's total volume, and value B[i] which describes
# the volume of the empty space inside it.

# We call a sub-set of cubes Beautiful if it satisfies the following 2 conditions
# 1. All its cubes can be ordered in some way such that they can be nested
# inside each other. This means that B[i] >= A[i+1] for all (1 <= i < M)
# such that M is the number of chosen cubes in the subset.
# 2. The length of the sub-set is the largest we can get which means no un-
# chosen cube can be added to this sub-set at some position still satisfying point 1.

# We define the Value of a Beautiful sub-set of cubes as the total empty space
# inside the whole built structure. le., B[i] - A[i+1] + ... + B[M]
# Find the total number of Beautiful subsets of cubes with the minimum
# possible Value. Since the answer can be large return it modulo 10^9+7

# The two subset are considered different if there exists at least one index i
# such that one of the subsets contains ith cube and another subset doesn't
# It is given that Array[i][0] = A[i] and Array A[i][1] = B[i]

# Input Format
# The first line contains an integer, N, denoting the number of rows in Array
# The next line contains an integer. M. denting the number of columns in Aray
# Each line I of the N subsequent line where (0 <= i < N) contains M space
# separated integers each describing the row Array[i]

# 3           1
# 2
# 2 1
# 3 2
# 4 3

# There is only one way which is to take the whole cubes and they can be 
# nested inside each other with the following order: 3 -> 2 -> 1

# 4            2
# 2
# 2 1
# 3 2
# 3 2
# 4 3

# 4 -> 3 -> 1
# 4 -> 2 -> 1 ie 2 ways