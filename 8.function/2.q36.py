"""
Write a function that print all the factors of a number entered by user
"""
def print_number():
    num=int(input("Enter a nnumber"))
    for i in range(1,num+1):
        if num%i==0:
            print(i, end=" ")
print_number()
print_number()
