"""
Q2. Take the length and width of a rectangle and calculate its area.
"""
length=int(input("Enter the length"))
width=int(input("Enter the width"))
area=length*width
print(f"area= {area}")

def reactangle_of_area():
    length=int(input("Enter the length"))
    width=int(input("Enter the width"))
    area=length*width
    print(f"area= {area}")
reactangle_of_area()

def reactangle_of_area(length,width):
    return length*width
print(reactangle_of_area(3,3))
