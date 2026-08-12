""" Take a number as input. Print the result of that number raised to the
power of 3 using **. Also print what // 7 and % 7 give for the same number."""

number=int(input("Enter a number"))
print(f"cube of {number} = {number**3}")
print(f"floor division of {number} by 7 is {number//7}")
print(f"remainder of {number} by 7 is {number%7}")