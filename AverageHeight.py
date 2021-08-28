Height=input("Enter the height pof different students: ").split()
sum=0
c=0
for i in Height:
    c=c+1
    sum+=int(i)

print(sum/c)