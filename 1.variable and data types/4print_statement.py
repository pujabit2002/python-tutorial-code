name="kumu"
age=26
gender="male"
print("hello")
print("hello" , name)
print("hello", name,"your age is", age, "and gender is", gender)

"""print("hello "+ name +" and gender is "+gender)
iska output hota hai:- hello kumu and gender is male
"""

"""
print("hello"+name+"and gender is"+gender+"and your is"+age)
output:- error print karega . kyuki "and your is" string hai usko hmm age(int) ke sath add nhi kr askte hai
"""

print(name,age, gender, sep='_')
"""output:- kumu_26_male"""
print(name, age,gender,sep="abc")
"""output:- kumuabc26abcmale """
print(name, end="")
print(age, end=" ")
print(gender)




# F-Strings , format
print(f"your name is {name}, age is {age} , gender is {gender}")
"""output:-  your name iskumu, age is 26 , gender is male"""

print(f"name is {name}, age is {age+30}, gender is {gender}")
"""outpuut:-  name is kumu, age is 56, gender is male """