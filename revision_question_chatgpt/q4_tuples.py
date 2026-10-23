sales=[("Laptop", 50000),
("Mouse", 800),
("Keybord", 1500),
("Monitor", 12000),
("USB Cable", 300)
]
total=0
count=0
for i in range(0,5):
    print(f"{sales[i][0]} : {sales[i][1]}")
    x=sales[i][1]
    if x>=1000:
        count=count+1
    total=total+x

print(total)
print(f"Product with sales>= 1000:{count}")