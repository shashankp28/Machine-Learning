from time import time

with open("keylog.txt", "r") as f:
    data = [x.strip().split() for x in f.readlines()]
    data = [(x[0], float(x[1])) for x in data]

_, base = data[0]
data = [(data[0], data[1] - base) for data in data[1:]]
with open("keydata.txt", "w+") as f:
    for d in data:
        f.write("{}\n".format(d[1]))
