#    -13-12 -11 -10-9--8 -7 -6 5- -4 -3 -2 -1
#     0  1 2 3   4. 5 6.  7 8. 9. 10 11 12
lst=[34,2,5,49,60,20,39,10,29,39,40,73,59]
#lst1=lst[1:14]     
#print(lst1)           output:- error

#lst1=lst[5:10]
#print(lst1)     #output:-[20, 39, 10, 29, 39]

#lst1=lst[3:11]
#print(lst1)     #output:-[49, 60, 20, 39, 10, 29, 39, 40]

#lst1=lst[1:88]
#print(lst1)     #output:-[2, 5, 49, 60, 20, 39, 10, 29, 39, 40, 73, 59]

#lst1=lst[5:6]
#print(lst1)     #outpput:-[20]

#lst1=lst[5:5]
#print(lst1)     #output:-[]

#lst1=lst[4:]
#print(lst1)     #output:-[60, 20, 39, 10, 29, 39, 40, 73, 59]

#lst1=lst[:3]
#print(lst1)     #output:-[34, 2, 5]

#lst1=lst[0:9:2]
#print(lst1)     #output:-[34, 5, 60, 39, 29]

#lst1=lst[0::2]
#print(lst1)     #output:-[34, 5, 60, 39, 29, 40, 59]

#.  -10 -9  -8. -7. -6.  -5. -4. -3. -2. -1
#.   0.  1.  2.  3.  4.   5.  6.  7.  8.  9
lst=[56, 78, 89, 23, 49, 69, 38, 45, 28, 29]
lst1=lst[9:3:-1]
print(lst1)
lst1=lst[5:1:-1]
print(lst1)
lst1=lst[::-1]
print(lst1)
lst1=lst[::-2]
print(lst1)