""" Take the user
'
s age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results."""
age=int(input("Enter the age"))
if (age>=18):
    print("eligible to vote")
    if(age>=60):
        print("they are a senior citizen")
else:
    print("Not eligible to vote")