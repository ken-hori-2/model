import random

# # 1～6の目が出るサイコロ(dice)を用意
# dice = list(range(1,7))

# print(dice)

# # 6の目が出やすいように重みを設定する
# # w = [1, 1, 1, 1, 1, 2]
# w = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# w = [0.4, 0.2, 0.1, 0.1, 0.9, 1.0]

# # 歪んだサイコロを1000回振ってサンプルを得る
# samples = random.choices(dice, k = 1000, weights = w)

# # 結果の確認
# for i in dice:
#   print(i, ':', samples.count(i))



import matplotlib.pyplot as plt

# # ヒストグラムを描画
# plt.hist(samples, bins=6, ec = 'black')
# plt.show()

BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]

# w = [round(0.1 * random.randint(1, 10), 2) for x in range(len(BPLIST))]
w = [0.9, 0.4, 0.6, 0.2, 0.7]
print(f"w = {w}")
# w2 = [round(w[x] / (len(BPLIST)-x), 2) for x in range(len(BPLIST))]
# # w = [round((0.1 * random.randint(1, 10)) / x, 2) for x in range(len(BPLIST),1)]
# print(f"w2 = {w}")

samples = random.choices(BPLIST, k = 100, weights = w)
# print(f"SAMPLE:{samples}")

# 結果の確認
for i in BPLIST:
  print(i, ':', samples.count(i))

# ヒストグラムを描画
# plt.hist(samples, bins=5, ec = 'black')
# plt.show()

w2 = [round(w[x] / (len(BPLIST)-x), 2) for x in range(len(BPLIST))]
# w = [round((0.1 * random.randint(1, 10)) / x, 2) for x in range(len(BPLIST),1)]
print(f"w2 = {w2}")
samples = random.choices(BPLIST, k = 100, weights = w2)
# print(f"SAMPLE:{samples}")

# 結果の確認
for i in BPLIST:
  print(i, ':', samples.count(i))

# print("\n")
prob = [5,4,3,2,1]
# from operator import mul

# combined2 = map(mul, w, prob)
# print(f"w3 = {combined2}")

# 2 つのリストの要素同士の演算
w3 = [round(x/y, 2) for x,y in zip(w,prob)]
print(f"w3 = {w3}")

samples = random.choices(BPLIST, k = 100, weights = w3)
# print(f"w3 = {map(mul, w, prob)}")
# 結果の確認
for i in BPLIST:
  print(i, ':', samples.count(i))