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
        print(f"{target} not present in any list")
    
check_target([2,38,5,2],[12,30,56,75], 3)