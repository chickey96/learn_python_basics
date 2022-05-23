#!/usr/bin/env python
# function that sums diagonals of a 2D, square matrix
def calculate_diagonal_sum(square_matrix):
    total = 0
    r = 0
    # initialize left and right indices for columns
    c_left = 0
    c_right = len(square_matrix[0])-1

    # loop until an index is out of bounds  
    # (ok to check only r in square square_matrix, indices should all be either valid or invalid)
    while(r < len(square_matrix)):
        total += square_matrix[r][c_left]

        # check to avoid double counting center square
        if(c_left != c_right):
            total += square_matrix[r][c_right]
        # increment/decrement indices
        r += 1
        c_left += 1
        c_right -= 1

    return total

matrix1 =   [[1,2,3],
            [4,5,6],
            [7,8,9]]

matrix2 =   [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]

matrix3 = [[5]]

print(f'{calculate_diagonal_sum(matrix1)} should equal 25')
print(f'{calculate_diagonal_sum(matrix2)} should equal 8')
print(f'{calculate_diagonal_sum(matrix3)} should equal 5')

