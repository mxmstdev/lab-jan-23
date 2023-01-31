import ast
import random
from time import time


def merge(a, b):
    na, nb = len(a), len(b)
    ia, ib = 0, 0
    c = []
    while ia < na and ib < nb:
        if a[ia] < b[ib]:
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
    return c + a[ia:] + b[ib:]

def mergesort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    return merge(mergesort(a[:m]), mergesort(a[:m]))


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end='\n\n')
#
# a = qsort(a)
#
# print(' '.join(map(str, a)))

resf = open("../results/mergesort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    mergesort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    mergesort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)
