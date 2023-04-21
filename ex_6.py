#Iterator on String (characters)

a = "123456"
for c in a:
    print(c)

b = "  I like python "
for c in b:
    print(c)


#Iterator using next()
itr = iter(a)
print(itr)

try:
    while True:
        x = next(itr)
        print(x)
except StopIteration as e:
    print("Iteration ended")