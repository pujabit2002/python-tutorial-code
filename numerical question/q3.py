""" Take the user
'
s age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results."""
def age_vote():
    age=int(input("Enter the age"))
    if (age>=18):
        print("Eligible to vote")
        if (age>=60):
            print("they are a senior citizen")
    else:
        print("not eligible to vote")
age_vote()
