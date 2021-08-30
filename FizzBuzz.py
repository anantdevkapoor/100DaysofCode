x=1
while x!=101:
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")

    elif x%5==0:
        print("Buzz")
    if x%3!=0 or x%5!=0:
        print(x)
    x+=1



