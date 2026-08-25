"""
Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order. Print True if it is sorted, and False otherwise.
Do not use built-in sort or sorted() functions for checking.
"""

def is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if lst[i]>lst[i+1]:
            return False
    return True
nums=[2,4,6,8,60]
print(is_sorted(nums))


