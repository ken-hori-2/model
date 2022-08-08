import random

BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]
BPLIST = [5, 4, 3, 2, 1]

# w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
w = [0.8, 0.6, 0.2, 0.9, 0.4]
# prob = [5,4,3,2,1]

# w = [0.9, 0.4, 0.6, 0.2, 0.7]
# w = [1,1,1,1,1]
print(f"w = {w}")
samples = random.choices(BPLIST, k = 1000, weights = w)
# # 結果の確認
for i in BPLIST:
  print(i, ':', samples.count(i))

import matplotlib.pyplot as plt

# ヒストグラムを描画
plt.hist(samples, bins=5, ec = 'black', color="orange")
# plt.bar(test,height=1)
plt.show()

# w2 = [round(w[x] / (len(BPLIST)-x), 2) for x in range(len(BPLIST))]
# print(f"w2 = {w2}")
# samples = random.choices(BPLIST, k = 100, weights = w2)
# # 結果の確認
# for i in BPLIST:
#   print(i, ':', samples.count(i))


BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
BPLIST = [5, 4, 3, 2, 1, 0]
# nextbp = [0, 0] # [1, 0] # [3, 0]
nextbp = 0

bpindex = BPLIST.index(nextbp)
print(bpindex)
Arc = []
# Arc = [(abs(BPLIST[bpindex][0]-BPLIST[x][0])) for x in range(len(BPLIST))]
Arc = [(abs(BPLIST[bpindex]-BPLIST[x])) for x in range(len(BPLIST))]


print(Arc)
index = Arc.index(0)
Arc.pop(index)
print(Arc)

w = [round(1/Arc[x],2) for x in range(len(Arc))]
print(f"w = {w}")

BPLIST.pop(-1)
samples = random.choices(BPLIST, k = 1000, weights = w)
# # 結果の確認
for i in BPLIST:
  print(i, ':', samples.count(i))

# import matplotlib.pyplot as plt

# ヒストグラムを描画
plt.hist(samples, bins=5, ec = 'black', color="blue")
# plt.bar(test,height=1)
plt.show()