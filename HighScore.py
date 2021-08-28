Score=input("Enter the various High Score ").split()
High=0
for i in Score:
    i=int(i)
    if High<i:
        High=i

print(High)