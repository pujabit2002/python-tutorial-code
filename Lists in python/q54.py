"""
Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.

"""
def nums_target(lst,target):
    for item in lst:
        if target == item:
            return True
        return False
status=nums_target([11,20,30,40], 9)
print(status)


