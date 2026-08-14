"""
Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)
"""
total=0
while True:
    number=int(input("Enter a number= "))
    if number<0:
        continue
    if number==0:
        break
    total=total+number
print(total)

