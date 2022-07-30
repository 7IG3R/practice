# You are given two integer arrays A and B of size N.

# If at the time i you have array A then you get A; points otherwise you get B, points. The
# total score is defined as the sum of all points received from time 0 to time (N-1).

# Initially, you have array A but you can exchange array A with B at any time t. However if
# you have array B you cannot exchange it for array A
# Find the maximum total score you can have.
# Notes:
# • If you decide to exchange array A with B at time t, then at that time t, value of Bit]
# would be added to the score and not value of Alt]. E.g, if at time t=3 you decide to
# vath
# make an exchange, then B[3] would be added to score for t=3 and not A[3].
# Input Format
# The first line contains an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 si < N) contains an integer describing