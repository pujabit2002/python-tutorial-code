"""Q9: Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""
def grade():
    marks= int(input("Enter your marks"))
    if (marks>=90):
        print("Grade A")
    elif(marks>=75) and (marks<=89):
        print("Grade B")
    elif(marks>=60) and (marks<=74):
        print("Grade C")
    elif(marks>=40) and (marks<=59):
        print("Grade D")
    else:
        print("Grade F")
grade()