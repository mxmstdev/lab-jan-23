import os
import random

N = list(range(500, 10001, 500))

for k in N:
    dirpath = "arrs/" + str(k)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    fl = open(dirpath + '/reverse.txt', "w+")
    fl.write(str(list(range(k, 0, -1))))
    fl.close()
