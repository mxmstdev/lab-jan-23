import os
import random

N = list(range(500, 100001, 500))

for k in N:
    dirpath = "arrs/" + str(k)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    fl = open(dirpath + '/random.txt', "w+")
    fl.write(str([random.randint(-100_000, 100_000) for i in range(k)]))
    fl.close()
