import ast
import random
from time import time


def cntsort(a):
    c = [0] * (int(1e5) + 1)
    for x in a:
        c[abs(x)] += 1
    a = []
    for i in range(len(c)):
        a += [i] * c[i]
    return a


# a = [random.randint(-100_000, 100_000) for k in range(100)]
# print(a, end='\n\n')
#
# a = qsort(a)
#
# print(' '.join(map(str, a)))

resf = open("../results/cntsort.txt", "w+")

resf.write("rnd:    ")
print("rnd")

for i in range(5000, 50001, 5000):
    randfile = open("../arrs/" + str(i) + "/random.txt")
    randstr = str(randfile.read())
    randlist = list(ast.literal_eval(randstr))

    t0 = time()
    cntsort(randlist)
    t1 = time() - t0

    resf.write("{:.2f}".format(t1) + ";")
    print(i)

print("rev")
resf.write("\nrev:    ")

for i in range(5000, 50001, 5000):
    revlist = list(range(i, 0, -1))

    t0 = time()
    cntsort(revlist)
    t2 = time() - t0

    resf.write("{:.2f}".format(t2) + ";")
    print(i)
