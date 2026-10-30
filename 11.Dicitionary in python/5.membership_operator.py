student={"name":"Kumu", "age":25, "city":"Bihar"}
print("age" in student)
print(35 in student)
print("phone no" not in student)

student1={"name":"Kupu", "age": 22, "city":"Bihar"}
k=input("Enter key =")
if k in student:
    print(student[k])
else:
    print("key does not exits")