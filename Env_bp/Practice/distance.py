import numpy as np

a = np.array([1, 1])
b = np.array([2, 2])

d = np.linalg.norm(a-b)

print(d)

BPLIST = np.array([[5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
BPLIST = np.array([[5, 0], [4, 0], [3, 0], [2, 0], [2, 1], [2, 2],[2, 3], [1, 0]])
# BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [2, 1], [2, 2],[2, 3], [1, 0]]
# BPLIST = [5, 4, 3, 2, 1, 0]
nextbp = [0, 0] # np.array([0, 0]) # [1, 0] # [3, 0]
# nextbp = 0
nextbp = [2, 3]

# bpindex = BPLIST.index(nextbp)
# bpindex = (np.where(BPLIST == nextbp)[0][0])
bpindex = BPLIST.tolist().index(nextbp)
print("index:{}".format(bpindex))
Arc = []
Arc = [(abs(BPLIST[bpindex][0]-BPLIST[x][0])) for x in range(len(BPLIST))]
# Arc = [(abs(BPLIST[bpindex]-BPLIST[x])) for x in range(len(BPLIST))]

print(Arc)

Arc = [round((abs(np.linalg.norm(BPLIST[bpindex]-BPLIST[x]))), 3) for x in range(len(BPLIST))]

print(Arc)


from scipy.spatial import distance

# print(distance.euclidean(a, b))
BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [2, 1], [2, 2],[2, 3], [1, 0]]
Arc = [round((abs(distance.euclidean(BPLIST[bpindex], BPLIST[x]))), 3) for x in range(len(BPLIST))]

print(Arc)

from math import dist

Arc = [round((abs(dist(BPLIST[bpindex], BPLIST[x]))), 3) for x in range(len(BPLIST))]
print(Arc)

# test
import math

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

if __name__ == '__main__':
    # x1, y1, x2, y2 = 1.0, 2.0, 2.0, 3.0
    BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [1, 0]]
    bpindex = BPLIST.index([2, 3])
    # print(BPLIST[bpindex][0])
    # print(BPLIST[bpindex][1])
    # print(BPLIST[0][0])
    # print(BPLIST[0][1])

    # Arc = [round((abs(get_distance(BPLIST[bpindex], BPLIST[x]))), 3) for x in range(len(BPLIST))]
    # d = round(get_distance(BPLIST[bpindex][0], BPLIST[bpindex][1], BPLIST[0][0], BPLIST[0][1]), 3)
    d = [round(get_distance(BPLIST[bpindex][0], BPLIST[bpindex][1], BPLIST[x][0], BPLIST[x][1]), 3) for x in range(len(BPLIST))]
    print(d)