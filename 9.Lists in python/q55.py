"""
Given a list of numbers, use a loop to calculate and print their average. You can use len() to get the count of elements, but avoid using sum() for the total.
Format the average to two decimal places.
"""
def calculate_average(scores):
    n=len(scores)
    total=0
    for num in scores:
        total=total+num
    return total/n
scores = [85, 90, 78, 92, 88]
print(calculate_average(scores))