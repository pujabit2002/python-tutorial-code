""" Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator."""
def even_odd ():
    num= int(input("Enter the number"))
    if num%2==0:
        print(f"{num} is even number ")
    else:
        print(f"{num} is odd number")
even_odd()