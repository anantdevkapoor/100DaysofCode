#Iterator using tuple ( ) syntax

a = ("one", "two", "three", "four")
print(a)
for item in a:
    print(item)


#Iterator using next()
itr = iter(a)
print(itr)

try:
    while True:
        x = next(itr)
        print(x)
except StopIteration as e:
    print("Iteration ended")