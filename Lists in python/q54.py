"""
Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.

"""
from ast import List
def nums_target(lst,target):
    for item in lst:
        if target == item:
            return True


       
        return False


   

status=nums_target([11,20,30,40], 9)
# print(status)

# waf to check whether given both list are samae length or not

def check_list(lst1,lst2):
    length_lst1=len(lst1)
    length_lst2=len(lst2)
    if length_lst1==length_lst2:
        return True
    return False

status=check_list([3,54,76,85],[32,443,22,455])
if status:
    print("both list are same in length")
else:
    print("both list are not same in length")

#WAF to check whether given target lie in which list mention the list name if present in both mention both.
def check_target(lst1,lst2,target):
    found_in_lst1=False
    for item in lst1:
        if target==item:
            found_in_lst1=True

    found_in_lst2=False
    for item in lst2:
        if target==item:
            found_in_lst2=True

    if found_in_lst1==True and found_in_lst2==True:
        print(f"{target} Present in both")
    elif (found_in_lst1==True):
        print(f"{target} present in {lst1}")
    elif(found_in_lst2==True):
        print(f"{target} Present in{lst2}")
    else:
        print(f"{target} not present in")
    
check_target([2,38,5,2],[12,30,56,75], 3)
