"""
Take a number as input. Print whether it is positive, negative, or zero.

"""
def positive_negative_zero():
    number=int(input("Enter thr number"))
    if number>0:
        print ("positive number")
    elif number<0:
        print("negative number")
    else:
        print("Zero number")
positive_negative_zero()