import ast
import random
from time import time


def inssort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        t = a[i]
        while j > 0 and a[j - 1] > t:
            a[j] = a[j - 1]
            j -= 1
        a[j] = t


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end='\n\n')
#
# a = qsort(a)
#
# print(' '.join(map(str, a)))

resf = open("../results/inssort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    inssort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    inssort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)
