""" Take a number as input. Print the result of that number raised to the
power of 3 using **. Also print what // 7 and % 7 give for the same number."""
def power():
    number= int(input("Enter the number"))
    print(f" power = {number**3}")
    print(f"floor division {number//7}")
    print(f"remainder = {number%7}")
power()