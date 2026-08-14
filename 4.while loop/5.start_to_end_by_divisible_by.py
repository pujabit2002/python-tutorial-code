start=int(input("Enter start number"))
end=int(input("Enter end number"))
i=start
while i<=end:
    if i%3==0 and i%4==0:
        print(i, end = " ")
    i=i+1