"""
Q84. Top Scores
Populate a dicitionary with six student names and their corresponding marks.
Loop through it and print the names of all students who achieved a score above 75.
"""
students={
    "Alice":82,
    "Bob":67,
    "charlie":91,
    "Diana":74,
    "Eve":88,
    "Frank":55
}
for name,mark in students.items():
    if mark>=75:
        print(f"student = {name} and mark scored = {mark}")