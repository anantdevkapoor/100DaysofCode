print("Welcome to the Love Calculator")
name1=input("What is your Name").lower()
name2=input("What is their Name").lower()
t=(int(name1.count("t")))+(int(name2.count("t")))
r=(int(name1.count("r")))+(int(name2.count("r")))
u=(int(name1.count("u")))+(int(name2.count("u")))
e=(int(name1.count("e")))+(int(name2.count("e")))
l=(int(name1.count("l")))+(int(name2.count("l")))
o=(int(name1.count("o")))+(int(name2.count("o")))
v=(int(name1.count("v")))+(int(name2.count("v")))
e=(int(name1.count("e")))+(int(name2.count("e")))
sum1=t+r+u+e
sum2=l+o+v+e
sum=(sum1*10)+sum2
print(f"Your Compatibility is {sum}")
