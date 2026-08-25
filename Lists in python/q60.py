"""
Q60. Given two lists, merge them into a
single new list without modifying the
originals.
Hint: Use the + operator or a loop to
combine. Example: list1 = [1, 2], list2 = [3,
4] → merged = [1, 2, 3, 4]
"""
list1=[1,2]
list2=[3,4]
new_list=list1+list2
print(new_list)

def merge_two_lists(lst1,lst2):
    return lst1+lst2
num1=[1,2,3]
num2=[4,5,6]
print(merge_two_lists(num1,num2))


def merge_two_lists(lst1,lst2):
    new_list=[]
    for num in lst1:
        new_list.append(num)
    for num in lst2:
        new_list.append(num)
    return new_list

num1=[1,2,3]
num2=[4,5,6]
print(merge_two_lists(num1,num2))