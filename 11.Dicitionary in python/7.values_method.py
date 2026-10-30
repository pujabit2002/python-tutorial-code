marks={
    "science":99,
    "maths":100,
    "comp":88,
    "hindi":43,
    "history":71,
}
print(marks.values())
for mark in marks.values():
    print(mark)

marks1={"science":99, "maths":78, "comp":89, "hindi": 84, "history":56}
total=0
for mark in marks1.values():
    total=total+mark
print(total)