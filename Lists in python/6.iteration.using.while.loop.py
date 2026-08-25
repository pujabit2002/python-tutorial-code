
nums=[2, 4, 23, 26, 49, 59, 20, 46, 59, 89]
n=len(nums)
i=0
while i<n-1:
    print(nums[i], end= " ")
    i=i+1
print("")



nums=[2, 4, 23, 26, 49, 59, 20, 46, 59, 89]
n=len(nums)
i=0
count=0
while i<=n-1:
    if nums[i]%2==0:
        count+=1
    i+=1
print(count)




nums=[2, 40, 23, 26, 49, 59, 20, 46, 59, 89]
n=len(nums)
i=n-1
while i>=0:
    print(nums[i], end= " ")
    i=i-1
