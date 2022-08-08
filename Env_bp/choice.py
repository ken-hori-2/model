import random

# BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]

# w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
# prob = [5,4,3,2,1]

# # w = [0.9, 0.4, 0.6, 0.2, 0.7]
# # w = [1,1,1,1,1]
# print(f"w = {w}")
# # samples = random.choices(BPLIST, k = 100, weights = w)
# # # 結果の確認
# # for i in BPLIST:
# #   print(i, ':', samples.count(i))

# # w2 = [round(w[x] / (len(BPLIST)-x), 2) for x in range(len(BPLIST))]
# # print(f"w2 = {w2}")
# # samples = random.choices(BPLIST, k = 100, weights = w2)
# # # 結果の確認
# # for i in BPLIST:
# #   print(i, ':', samples.count(i))




# # 2 つのリストの要素同士の演算
# w3 = [round(x/y, 3) for x,y in zip(w,prob)]
# print(f"w * prob = {w3}")

# samples = random.choices(BPLIST, k = 1000, weights = w3)

# # import numpy as np
# # test = np.zeros(shape=6)
# # 結果の確認
# for i in BPLIST:
#   print(i, ':', samples.count(i))
# #   test[i] = samples.count(i)

# # import matplotlib.pyplot as plt
# # # ヒストグラムを描画
# # # plt.hist(test, bins=5, ec = 'black')
# # plt.bar(test,height=1)
# # plt.show()
# samples = random.choices(BPLIST, k = 5, weights = w3)
# print(samples)

# prob = [len(BPLIST)-x for x in range(len(BPLIST))]
# print(prob)

# samples = random.choices(BPLIST, k = 1, weights = w3)
# print(f"test{samples[0]}")
# print(f"BPLIST={BPLIST}")
# print(prob)
# print(f"index:{prob.index(samples[0][0])}")
# # print(f"index:{BPLIST.index(samples[0][0])}")

# prob.remove(prob[prob.index(samples[0][0])])
# BPLIST.remove(samples[0])
# print(f"BPLIST(remove):{BPLIST}")
# # prob.remove(BPLIST[samples])
# print(f"prob(remove)={prob}")

# state = [3, 0]
# print(type(state))
# if samples[0] > state:
#     print("break")


# BPLIST = []

# print(len(BPLIST))

print("#################")
BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]
w = [0.9, 0.4, 0.6, 0.2, 0.7]
print("w:        {}".format(w))
test = random.choices(BPLIST, k = 1, weights = w)
print("test:{}".format(test[0][0]))
# print("index:{}".format(w[w.index(test[0][0])]))
# w.remove(w[w.index(test[0][0])])
# print("index:{}".format(w.index(test[0][0])))
bpindex = BPLIST.index([3, 0])
print("bpindex:{}".format(bpindex))
print("index:{}".format(w.index(w[bpindex])))

# w.remove(w[w.index(test[0][0])])
w.pop(bpindex)
print("w(remove):{}".format(w))


print("#################")
BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]
# test = random.choices(BPLIST, k = 1, weights = w)
# print("test:{}".format(test[0][0]))
nextbp = [1, 0] #[3, 0]
bpindex = BPLIST.index(nextbp)
print(bpindex)

# Arc = [ for x in BPLIST]
Arc = []
# print(BPLIST[bpindex][0])
# print(type(BPLIST[bpindex][0]))
# print(BPLIST[0][0])
# print(type(BPLIST[0][0]))

# for x in range(len(BPLIST)):
#     Arc.append(abs(BPLIST[bpindex][0]-BPLIST[x][0]))
#     # print(BPLIST[bpindex][0]-BPLIST[x][0])
# [Arc.append(abs(BPLIST[bpindex][0]-BPLIST[x][0])) for x in range(len(BPLIST))]
Arc = [(abs(BPLIST[bpindex][0]-BPLIST[x][0])) for x in range(len(BPLIST))]


print(Arc)
index = Arc.index(0)
Arc.pop(index)
print(Arc)