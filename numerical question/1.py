"""  Take two numbers as input from the user. Print their sum, difference,
product, and remainder."""
def two_numbers():
    num1=int(input("Enter the 1st number"))
    num2=int(input("Enter the 2nd number"))
    print(f" sum of = {num1+num2}")
    print(f" difference of = {num1-num2}")
    print(f" product of = {num1*num2}")
    print(f" remainder of = {num1%num2}")
two_numbers()