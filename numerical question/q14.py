# WAF to check whether given both list are samae length or not

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

