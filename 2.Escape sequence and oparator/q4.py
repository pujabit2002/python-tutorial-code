""" A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string."""
subject1=int(input("enter the marks1"))
subject2=int(input("enter the marks2"))
subject3=int(input("enter the subject3"))
total= subject1+subject2+subject3
average=total/3
print(f"total={total} and average={average}")