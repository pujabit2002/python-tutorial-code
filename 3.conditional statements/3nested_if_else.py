age=int(input("Enter your age"))
certificate=True
if (age>=18):
    if certificate==True:
        print("you will be hired")
    else:
        print("cannot hire due to you certificate")
else:
    print("cannot hire,age is less than 18")