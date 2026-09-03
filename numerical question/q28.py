"""
5
5 4
5 4 3
5 4 3 2 
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
def pattern_based():
    for i in range(5,0,-1):
        for j in range(5,i-1,-1):
            print(j, end=" ")
        print()

    for i in range(1,5):
        for j in range(5,i,-1):
            print(j, end=" ")
        print()
pattern_based()


#2nd method
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()

for i in range(2,7):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()
