student_name=input("Enter the student namea")
age=int(input("Enter the age"))
exam_percentage=float(input("Enter the exam percentage marks"))
fee_response=input("Is the fee paid?(yes/no):")
fee_Paid=fee_response=="yes"

print(f"Student name = {student_name}")
print(f"age = {age}")
print(f"exam percentage = {exam_percentage}")
print(f"fee paid yes or no {fee_Paid}")
print(type(student_name))
print(type(age))
print(type(exam_percentage))
print(type(fee_Paid))