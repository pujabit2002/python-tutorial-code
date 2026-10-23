student=("Alice", 85, 100)
marks_obtained=student[1]
maximum_maarks=student[2]
percentage=(marks_obtained/maximum_maarks)*100
print(f"student: {student[0]}")
print(f"Percentage: {percentage}")
if(percentage>=40):
    print("pass")
else:
    print("fail")

