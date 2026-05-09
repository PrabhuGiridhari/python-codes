d_3 = "Fizz"
d_5 = "Buzz"
d_3_5 = "FizzBuzz"

for n in range (1,101):

    if n % 3 == 0 and n % 5 == 0:
        print(d_3_5)
    elif n % 3 == 0:
        print(d_3)
    elif n % 5 == 0:
        print(d_5)
    else:
        print(n)
