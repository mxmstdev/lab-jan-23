import ast
import random
from time import time


def bubblesort(a):
    n = len(a)
    f = False
    while not f:
        f = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f = False


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end='\n\n')

resf = open("../results/bubblesort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    bubblesort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    bubblesort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)