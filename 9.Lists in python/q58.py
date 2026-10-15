lst=[3,-1,4,1,5]

maxi=float("-inf")
for num in lst:
    if num>maxi:
        maxi=num
print(f"maximum number = {maxi}")


mini=float("inf")
for num in lst:
    if num<mini:
        mini=num
print(f"minimum number = {mini}")