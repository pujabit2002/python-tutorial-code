"""
1
2 1
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
for i in range(1,6):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()


# 2nd method
n=int(input("Enter the number= "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()