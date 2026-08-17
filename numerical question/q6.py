""" Take two numbers as input. Without using *
, calculate and print their product
using += in a way that adds the first number to itself the
second number of times. (Think carefully.)"""

def calculate_add():
    num1=int(input("Enter the first number= "))
    num2=int(input("Enter the second number= "))
    product=0
    for i in range(1,num2+1):
        product=product+num1
    print(f"product of {num1} of {num2} without using * = {product}")
calculate_add()