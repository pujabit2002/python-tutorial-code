# 3 int as a parameter, print the total.
def add (a,b,c):
    ans=a+b+c
    print(f"total = {ans}")
add(10,12,45)
add(17,28,49)


# Ask a name, age,gender,print
#1st method
def greet(name, age, gender):
    print(f"Hey {name}! your age is {age} and gender is {gender}")
greet("puja", 18,"female")

#2nd method
def greet(name, age, gender):
    print(f"Hey {name}! your age is {age} and gender is {gender}")
n=input("Enter name= ")
a=int(input("Enter age= "))
g=input("Enter gender= ")
greet(n,a,g)