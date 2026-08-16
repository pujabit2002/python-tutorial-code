def fizzbuzz_function(n):
    if n%3==0 and n%15!=0:
        print("Fizz")
    elif n%5==0 and n%15!=0:
        print("Buzz")
    elif n%15==0:
        print("FizzBuzz")
    else:
        print(n)
fizzbuzz_function(8)