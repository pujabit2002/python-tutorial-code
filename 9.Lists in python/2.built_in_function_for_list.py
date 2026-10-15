marks=[23, 45,76, 46, 78,84, 28]
# To get the length
n=len(marks)
print(f"Length of list = {n}")

#max
maxi=max(marks)
print(f"Maximum marks = {maxi}")

#miin
mini=min(marks)
print(f"Minimum marks = {mini}")

#sum
total=sum(marks)
print(f"Total marks ={total}")

#To sort using sorted(), it will always return you a new list.total
new_list=sorted(marks)
print(f"new_list={new_list}")
print(f"marks ={marks}")


#To sort using sorted(), it will always return you a new list.total
new_list=sorted(marks,reverse=True)
print(f"new_list={new_list}")