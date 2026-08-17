""" A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string."""
def marks_scored():
    marks1=int(input("Enter the marks1"))
    marks2=int(input("Enter the marks2"))
    marks3=int(input("Enter the marks3"))
    total= marks1+marks2+marks3
    print(f"total = {total}")
    print(f"average = {total/3}")
marks_scored()