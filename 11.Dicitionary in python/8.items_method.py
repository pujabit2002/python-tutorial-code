marks={
    "science":99,
    "maths":100,
    "comp":88,
    "hindi":43,
    "history":71,
}
print(marks.items())

for detail in marks.items():
    print(detail)
print()
for detail in marks.items():
    print(detail[0])
print()
for detail in marks.items():
    print(detail[1])
print()
for detail in marks.items():
    sub=detail[0]
    mark=detail[1]
    print(sub,mark)


for sub, mark in marks.items():
    print(f"sub = {sub} and mark = {mark}")

for key in marks:
    print(key)
