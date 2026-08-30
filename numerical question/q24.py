"""
1
2 1
3 2 1 
4 3 2 1 
5 4 3 2 1
"""

def pattern_based_question():
    for i in range(1,6):
        for j in range (i,0,-1):
            print(j,end=" ")
        print()
pattern_based_question()


# 2nd method
def pattern_based():
    n=int(input("Enter the number= "))
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j, end=" ")
        print()
pattern_based()