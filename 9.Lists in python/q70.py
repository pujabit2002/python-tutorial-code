"""
Question 70
Given a 3x3 matrix, print its upper triangle. Replace all elements in
the lower triangle (below the main diagonal) with an asterisk (*).
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Expected Output:
# 1 2 3
# * 5 6
# * * 9
"""

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

#1st method
r=len(matrix)
c=len(matrix[0])
for i in range(0, r):
    for j in range(0,c):
        if i>j:
            matrix[i][j]="*"
        print(matrix[i][j], end=" ")
    print()


#2nd method
r=len(matrix)
c=len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if i<=j:
            print(matrix[i][j], end= " ")
        else:
            print("*", end=" ")
    print()


sales=[1200,800,2500,1500,600,3200,900,1000]
g=len(sales)
count=0
total=0
for num in range(0,g):
    if sales[num]>=1000:
        count=count+1
        total=total+sales[num]

print(count)
print(total)



temperatures=[32,35,31,39,36,41,34]
max1=temperatures[0]
count_days=0
for f in range(1,len(temperatures)):
    if temperatures[f]>max1:
        max1=temperatures[f]
    if temperatures[f]>=35:
        count_days=count_days+1
print(max1)
print(count_days)

mixi=max(temperatures)
print(mixi)




