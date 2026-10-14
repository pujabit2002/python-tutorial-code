"""
Question 68
Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements.
 Example:
 matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9] ]
Expected output for this example: 45
"""
matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9] ]
rows=len(matrix)
column=len(matrix[0])
sum=0
for i in range(0,rows):
    for j in range(0,column):
        sum=sum+matrix[i][j]
print(sum)
