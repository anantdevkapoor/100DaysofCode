Year=int(input("Please Enter the Year you want to check ")
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print(f"{Year} is a Leap Year")
        else :
            print(f"{Year} is not a Leap Year")
    else :
        print(f"{Year} is a leap Year")
else:
    print(f"{Year} is not a leap Year)