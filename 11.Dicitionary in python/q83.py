#question 83
"""
Subject Performance Analysis:-
Given a dictionary of marks for different subjects loop over its values() to
calculate and print the total marks and the average mark obtained
"""

marks={"maths":99, "sciende":76, "English":91, "history":65, "computer":95}

#1st method
total_subjects=len(marks)
total_marks=sum(marks.values())
print(total_marks)
print(f"Avg = {total_marks/total_subjects}")

#2nd method
total_subject=len(marks)
total=0
for mark in marks.values():
    total=total+mark
print(f"avg = {total/total_subject}")