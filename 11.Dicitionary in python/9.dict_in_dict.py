student={
    "101":{"name":"Rahul", "age":21, "city":"Delhi"},
    "102":{"name":"Priya", "age":20, "city":"Mumbai"},
    "103":{"name":"Karan", "age":22, "city":"Pune",
    "details":{"ph":81881, "gender":"Male"}},
}
#How to access

print(student["101"])
print(student["101"]["name"])
print(student["103"]["city"])
print(student["103"]["details"])
print(student["103"]["details"]["gender"])

for roll_no, details in student.items():
    print(f"roll_no = {roll_no} and details = {details}")

for roll_no, details in student.items():
    print(f"roll_no = {roll_no}, name = {details['name']}, age = {details['age']}")

total=0
for rollno, details in student.items():
    total=total+details['age']
print(total)