# Print all the numbers which are divisible by 3 and 5, from 1 to 100.
num=int(input("enter the number"))
i=1
while(i<=100):
    if (i%3==0 and i%5==0):
        print(i)
    i=i+1