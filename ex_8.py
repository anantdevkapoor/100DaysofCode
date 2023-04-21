#iterator on list using next()


a = ["one", "two", "three", "four"]

itr = iter(a)
print(itr)

try:
    while True:
        x = next(itr)
        print(x)
except StopIteration as e:
    print("Iteration ended")




