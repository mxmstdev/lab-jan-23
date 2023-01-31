import ast
import random
from time import time


def selsort(a):
    n = len(a)
    for i in range(n):
        imin = i
        for j in range(i + 1, n):
            if a[imin] > a[j]:
                imin = j
        
        a[imin], a[i] = a[i], a[imin]


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end = '\n\n')
#
# selsort(a)
#
# print(' '.join(map(str, a)))

resf = open("../results/selsort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    selsort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    selsort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)