## Exercise 2
#
# 1) Change the sign of the elements of the matrix accordingly with the given sign_matrix
# For example:
#   1  2     + -     --->     1 -2
#  -2  3  ,  - +     --->     2  3
#
# 2) Sum all the elements for any row (i) and add the result to the column (i)
# For example
#   1 -2   ->   -1   ->   0  3
#   2  3   ->    5   ->   1  8
#
# 3) the solution is the string value of the matrix =>  str(result_matrix)
#
# To check the correctness of your solution
# python3 test.py -2 "solution"
#

matrix = [[ 1, -2, 4, 0, -1], [ 2, 9, -6, 1, 0], [ -3, -1, 6, 2, 5], [ 0, 8, -4, -4, 1], [7, -7, 1, 5, -2]]
sign_matrix = matrix = [["+", "-", "-", "+", "+"], ["+", "-", "+", "-", "+"], ["-", "+", "-", "+", "+"], ["+", "-", "-", "-", "+"], ["+", "-", "+", "+", "+"]]
result_matrix = []

# ...
# ...
# ...

print(result_matrix)