#start and end , print start to end

start=int(input("Enter start number= "))
end=int(input("Enter ened number= "))
for i in range(start, end+1):
    print(i, end=" ")
print("\n")



# sum of total number
total=0
for i in range(start,end+1):
    total=total+i
print(total)