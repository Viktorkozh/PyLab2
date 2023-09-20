import timeit

def f():
    j = 0
    for i in range(1000):
        j += 1

for i in range(100):
    print("Something number", i)

med = 0

for i in range(10000):
    med += timeit.timeit(lambda: f(), number=1)
med /= 10000
print("Python can count to 2000 in", med)
