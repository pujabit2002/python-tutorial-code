#pop Method
student={"name":"Rahul","age":35, "gender":"Male", "city":"Surat"}
print(student,id(student))
student.pop("name")
print(student,id(student))
#agar jo key exits nhi karta hai usko hmm pop nhi kr sakte hai kyuki wo error print karta hai ex: print(studennnnt,id(student))


#clear method ex: student1.clear()
student1={"name":"kumu", "age": 25, "city":"Patna"}
student1.clear()
print(student1)


student2={"name":"mithu", "age":3, "city":"Patna"}
del student2
#aur hmm yaha par print bhi nhi kr sakte hai kyuki student2 ka name ka variable pura delete ho gaya hai. (agar parint kiye tho error dega)


student3={"name":"mithu", "age":3, "city":"Patna"}
del student3["age"]
print(student3)