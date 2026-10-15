matrix=[
    [4,8,1], 
    [9,7,2], 
    [5,6,0],]

# 1st solution
print(matrix)
print(type(matrix))
print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

#2nd solution
for i in range(0,3):
    for j in range(0,3):
        print(matrix[i][j], end=" ")
    print()


#3rd solution
total=0
for i in range(0,3):
    for j in range(0,3):
        total=total+matrix[i][j]
print(total)