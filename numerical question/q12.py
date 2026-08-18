"""
Q13: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line.
"""
def using_ternary_operator():
    number=int(input("Enter the number"))
    status= "Even" if number%2==0 else "odd"
    print(status)
using_ternary_operator()