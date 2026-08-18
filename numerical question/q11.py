"""
Q12: Take three numbers as input. Print the largest of the three without using any
built-in function.

"""

def largest_of_three_numbers():
    num1=int (input("Enter the 1st number"))
    num2=int(input("Enter the 2nd number"))
    num3=int(input("Enter the 3rd number"))
    if ((num1>num2) and (num1>num3)):
        print("num1 is largest number")
    elif(num2>num3):
        print("num2 is largest")
    else:
        print("num3 is largest number")
largest_of_three_numbers()