#note:- hmm isko index se value ko access nhi kr sakte hai 
#note:- hmm isko key se value ko access karte hai.

marks={
    "science":99,
    "maths":100,
    "comp":88,
    "hindi":43,
    "history":71,
    1:10
}
print(marks["science"])
print(marks[1])

print(marks.get("science"))
print(marks.get("scienceee"))
print(marks.get("scienceee", 1))

subject="history"
ans=marks.get(subject)
if ans is None:
    print("subject not found")
else:
    print(f"marks scored={ans}")