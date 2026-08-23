"""
Q1. Take two integers from the user and print their:
sum
difference
product
division
"""

"""#1st method
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print(f"sum = {num1+num2}")
print(f"difference = {num1-num2}")
print(f"product = {num1*num2}")
print(f"division = {num1/num2}")


#2nd method
def sum_difference_product_division():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    print(f"sum = {num1+num2}")
    print(f"difference = {num1-num2}")
    print(f"product = {num1*num2}")
    print(f"division = {num1/num2}")
sum_difference_product_division()"""

#3rd method
def sum_difference_product_division():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    sum=num1+num2
    difference=num1-num2
    product=num1*num2
    division=num1/num2
    return sum, difference, product, division

sum, diff, prod, div=sum_difference_product_division()
print(f"sum = {sum}")
print(f"difference={diff}")
print(f"product={prod}")
print(f"division={div}")


#4th method
def sum_difference_product_division(num1,num2):
    sum=num1+num2
    diff=num1-num2
    product=num1*num2
    division=num1/num2
    return sum,diff,product,division
result=sum_difference_product_division(10,2)
print(f"sum={sum}")