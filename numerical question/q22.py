"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""
def pattern_based_question():
    for i in range(5,0,-1):
        for k in range(1,i):
            print(" ", end=" ")
        for j in range(5,i-1,-1):
            print(j,end=" ")
        print()
pattern_based_question()