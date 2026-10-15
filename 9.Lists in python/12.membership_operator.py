nums=[1,4,1,2,5,1,5,3,1,2,1,3,6,1]
print(4 in nums)
print(8 in nums)



#question 
nums=[1,4,1,2,5,1,5,3,1,2,1,3,6,1]
target=int(input("Enter target = "))
if target in nums:
    nums.remove(target)
    print(f"nums = {nums}")
else:
    print("cannot remove target, target does not exits")