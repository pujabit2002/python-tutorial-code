"""
Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.
numbers=[3,1,4,1,5,9,2,6]
"""
numbers=[3,1,4,1,5,9,2,6]
maxi=float("-inf")
for num in numbers:
    if num>maxi:
        maxi=num
print(f"Maximum number = {maxi}")