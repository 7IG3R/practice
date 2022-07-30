# You are given a tree T with N nodes, rooted at node 0.
# Each node has a number written on it, represented by the array A. You can do the
# following operation any number of times on any subtree that includes the root:

# Add x (-1 <= x <= 1) to all of the numbers written on the vertices of the subtree.
# Find the minimum number of operations required to make the numbers on all the nodes
# of the tree equal to 0.

# Notes:
# • Every node has a parent node, except for the root.
# • You are given a parent array P as input where P, denotes parent of ith node.
# • It is given that P[0] = -1 since it is the root.

# Input Format
# The first line contains an integer, N, denoting the number of elements in P.
# Each line i of the N subsequent lines (where 0 <= i < N) contains an integer describing P[i]
# Each line i of the N subsequent lines where O <= i < N  contains an integer describing A[i]
# 3             3
# -1
# 0
# 0
# 1
# -1
# 1

# Tree has 3 nodes, 2 edges: (0, 1), (0, 2).
# Numbers on the node are 1, -1, 1. We would have to do 3 operations: 
# 1 Consider the subtree (0, 1) and add 1. 
# 2. Consider the subtree (0, 2) and add -1. 
# 3. Consider the subtree (0) and add 1.

