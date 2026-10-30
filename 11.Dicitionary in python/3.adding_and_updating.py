student={"name":"kumu", "age":21}
print(student,id(student))
# update
student["age"]=30
print(student,id(student))


student1={"name":"kuppu", "age":21}
print(student1, id(student1))
#Add
student1["gender"]="Male"
print(student1)

#update
# agar bahut saara key value ek hi saath dena hai tho hmm update use kr sakte hai.
student1.update({"city":"surat", "phone":912828238222232, "state":"BIhar","age":67})
print(student1)


#Note:agar hmm dicitionary mai ek hi name ka 2 key vallue hai tho wo key last bala value lega.
student1={"name":"kuppu", "age":21, "city":"bihar", "age":45}
print(student1)

