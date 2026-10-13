"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate.
"""

marks=[2,1,3,6,8,7,9,2,2]
n=len(marks)
print(f"first element = {marks[0]}")
print(f"middle elemnt = {marks[n//2]}")
print(f"last element = {marks[-1]}")
movies=["Housefull", "Dhurandhar", "Border", "Dhamal", "kakuda"]
print(movies[0])
print(movies[2])
print(movies[4])

print(movies[-1])
print(movies[-3])
print(movies[-5])
