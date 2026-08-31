"""
Write a Python script that iterates through a list of integers and
replaces every negative number found in the list with the value 0.
numbers = [5,-3, 8,-1, 0,-10, 12]
# Expected output: [5, 0, 8, 0, 0, 0, 12]
"""
import numbers
def replace_negative(lst):
    n=len(lst)
    for i in range(0,n):
        if lst[i]<0:
            lst[i]=0
    return lst
numbers=[2,1,3,1,3,-1,23,-32,-12,44]
print(replace_negative(numbers))
