"""
Question 67
Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75.
# Example input:
marks = [65, 80, 70, 90, 75, 82, 60]
"""

marks=[65,80,70,90,75,82,60]
new_list=[num for num in marks if num>=75]
print(new_list)
