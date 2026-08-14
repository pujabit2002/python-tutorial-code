# Ask a number from the user, print the multiplication table upto 10.
number=int(input("Enter the number"))
i=1
while i<11:
    print(f"{number} * {i} = {number*i}")
    i=i+1