import timeit

def f():
    j = 0
    for i in range(100000):
        j += 1
    print("end")

for i in range(100):
    print("Something number", i)

print("Python can count to 101000 in", timeit.timeit(lambda: f(), number=1))
