
# Iterator for dictionary using syntax { }

a = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

print(a)
for key in a:
    print(key, a[key])


#Iterator using next() on dictionary
itr = iter(a)
print(itr)

try:
    while True:
        x = next(itr)
        print(x, a[x])
except StopIteration as e:
    print("Iteration ended")