"""
Imagine you are developing a Python program for an online shopping website.

A customer purchases a pair of shoes and enters the following information:
- Product name
- Price per item
- Quantity purchased
Your program must collect this information, calculate the total bill, and display a clear purchase summary.
Your task
Write a Python program that:
1. Takes the product name from the user.
2. Takes the price per item as input.
3. Takes the quantity purchased as input.
4. Converts the price to a numeric data type and the quantity to an integer.
5. Calculates the total cost.
6. Prints the product name, price, quantity, and total bill.
"""
product_name=input("Enter the product name")
price_per_item=input("Enter the price per item")
quantity_purchased=input("Enter the quantity purchased")
x=float(price_per_item)
y=int(quantity_purchased)
total_bill=x*y
print(f" Product name = {product_name}")
print(f" price per item = {price_per_item}")
print(f"quantity purchased = {quantity_purchased}")
print(f"total bill = {total_bill}")