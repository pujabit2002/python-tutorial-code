"""
Question 69
Given a 3x3 matrix as input, print its lower triangle. Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Expected Output:
# 1 * *
# 4 5 *
# 7 8 9
"""
matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

#1st method
rows=len(matrix)
columns=(len(matrix[0]))
for i in range(0, rows):
    for j in range(0, columns):
        if i>=j:
            print(matrix[i][j], end=" ")
        else:
            print("*",end=" ")
    print()


#2nd method
rows=len(matrix)
column=len(matrix[0])
for i in range(0,rows):
    for j in range(0,column):
        if j>i:
            matrix[i][j]="*"
        print(matrix[i][j], end=" ")
    print()

