Size=input("What Size of Pizza Do you want? ")
Pep=input("Do you want peperoni Inside it? ")
ch=input("Do you want cheese inside it? ")
price=0
if Size=="L":
    price=25
elif Size=="M":
    price=20
elif Size=="S":
    price=15
else :
    print("Enter Valid Size")
if Pep=="Y" and Size=="S":
    price+=2
elif Pep=="Y":
    price+=3
if ch=="Y":
    price+=1

print(f"Your Bill is Worth $ {price}")