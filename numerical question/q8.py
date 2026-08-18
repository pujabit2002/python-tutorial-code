"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."""

def greater_of_the_number():
    num1=int(input("Enter 1st number"))
    num2=int(input("Enter 2nd number"))
    if (num1>num2):
        print(f"{num1} is greater than {num2}")
    elif(num1<num2):
        print(f"{num2} is greater than {num1}")
    else:
        print("both are equal")
greater_of_the_number()