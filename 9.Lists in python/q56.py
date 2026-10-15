"""
Given two lists of the same length, write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
"""
def sum_of_two_list(lst1,lst2):
    new_list=[]
    n=len(lst1)
    for i in range(0,n):
        total=lst1[i]+lst2[i]
        new_list.append(total)
    return new_list
list1=[10,20,30,40]
list2=[1,2,3,4]
ans=sum_of_two_list(list1,list2)
print(ans)