student_name=input("Enter the student namea")
age=int(input("Enter the age"))
exam_percentage=float(input("Enter the exam percentage marks"))
fee_Paid= bool(input("Enter the fee paid yes or no"))
if fee_Paid=="yes":
    print("True")
else:
    print("False")
print(f"Student name = {student_name}")
print(f"age = {age}")
print(f"exam percentage = {exam_percentage}")
print(f"fee paid yes or no {fee_Paid}")