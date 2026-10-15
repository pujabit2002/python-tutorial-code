# question:- make a new list from 1 to 10. -> [1,2,3,4..9,10]
#normal method
new_list=[]
for i in range(1,11):
    new_list.append(i)
print(new_list)

#list comprehension method
new_list=[i for i in range(1,11)]
print(new_list)


new_list=[x+7 for x in range(1,11)]
print(new_list)

new_list=[i*7 for i in range(1,8)]
print(new_list)

new_list=[i*i for i in range(10,0,-1)]
print(new_list)
