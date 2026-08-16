#Simple method
def square(num):
    return num*num
print(square(10))

#Lambda method
square=lambda num:num*num
print(square(5))
print(square(100))


#simple method
#Return True if age>=18 else False
def is_adult(age):
    if age>=18:
        return True
    return False
print(is_adult(20))

#lambda function
is_adult= lambda age: True if age>=18 else False
print(is_adult)