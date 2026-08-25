nums=[1,4,1,2,5,1,5,3,1,2,1,3,6,1]
#sort vs sorted
new_list=sorted(nums)
print(f"new_list = {new_list}", id(new_list))

print(f"nums={nums}", id(nums))
nums.sort(reverse=True)
print(f"nums={nums}", id(nums))