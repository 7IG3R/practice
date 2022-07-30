# Given an array A of Size N. You can perform any number of moves (possibly zero) for each
# element in the array A
# In one move, when you are at it index of the array A you can do either one of the following:
# You can jump to the index numbered i - A[i], as long as the value of i - A[i] >= 1.
# You can jump to the index numbered i + A[i], as long as the value of i + A[i] <= N.

# Assume that you are standing at an index i in the array A. Then, W
# denotes the minimum number of moves needed to reach an index j
# such that the parity of A[i] not equal to Al]. Let B be an array of size N
# such that B[i] denotes the value of W for the ith index in A[i]. It is given
# that B[i] = -1 for any index where it is not possible to meet the given condition.
