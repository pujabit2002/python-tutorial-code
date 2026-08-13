"""
age=int(input("Enter your age"))
if age>=18:
    status="Adult"
else:
    status="Minor"
print(f"your status is {status}")
"""


# using ternary opertaor
age1=int(input("enter your age"))
status="Adult" if age1>=18 else "Minor"
print(f"your status is {status}")