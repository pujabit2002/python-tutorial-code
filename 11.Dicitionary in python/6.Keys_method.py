marks={"science":99, "maths":100, "comp":88, "hindi":96, "history":43}
# keys ka kaaam hai ki jitne bhi keys hai usko list ke form mai share kr de .
print(marks.keys())


marks1={"science":99, "maths":100, "comp":88, "hindi":96, "history":43}
for sub in marks1.keys():
    print(f"subject = {sub} and marks = {marks1[sub]}")


marks2={"science":99, "maths":100, "comp":88, "hindi":96, "history":43}
total=0
for sub in marks2.keys():
    total=total+marks[sub]
print(total)