"""
 Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""
def find_max(a,b,c):
    if (a>b) and (a>c):
        print(f"{a} is greater ")
    elif (b>c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
find_max(9,78,3)
find_max(12,45,76)
