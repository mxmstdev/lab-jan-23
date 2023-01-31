import ast
import random
from time import time


def qsort(a):
    n = len(a)
    if n <= 1:
        return a
    m = random.choice(a)
    left = [x for x in a if x < m]
    eq = [x for x in a if x == m]
    right = [x for x in a if x > m]
    return qsort(left) + eq + qsort(right)


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end='\n\n')
#
# a = qsort(a)
#
# print(' '.join(map(str, a)))

resf = open("../results/qsort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    qsort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    qsort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)