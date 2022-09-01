



BPLIST = [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
BPLIST.pop(-1)
print("BPLIST : {}".format(BPLIST))




WEIGHT = [0.8, 0.6, 0.2, 0.9, 0.4]

print("WEIGHT : {} type:{}".format(WEIGHT, type(WEIGHT)))
 
print('・リストの要素が数値である場合')
WEIGHT_max = max(WEIGHT)
print("WEIGHT max : {}".format(WEIGHT_max))

INDEX = WEIGHT.index(max(WEIGHT))
print("index : {} type:{}".format(INDEX, type(INDEX)))

NEXT = BPLIST[INDEX]
print("next bp : {}".format(NEXT))

# まとめ
NEXT_BP = BPLIST[WEIGHT.index(max(WEIGHT))]
print("demo : {}".format(NEXT_BP))

#####
# Arc = [(abs(BPLIST[bpindex]-BPLIST[x])) for x in range(len(BPLIST))]
from sklearn import preprocessing
Arc = [5, 4, 3, 2, 1]
# Arc = [4, 3, 2, 1, 0]
Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
print(f"1/Arc = {Arc_INVERSE}")

# Arc の正規化
print("Arc:{}".format(preprocessing.minmax_scale(Arc)))


import numpy as np

# WEIGHT の正規化
print("WEIGHT:{}".format(np.round(preprocessing.minmax_scale(WEIGHT), 3)))

# WEIGHT2 = preprocessing.minmax_scale(WEIGHT)
# print(WEIGHT2, type(WEIGHT2))
# WEIGHT2 = np.round(WEIGHT2,3)
# print(WEIGHT2)











# test

# Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]


# # add 0808 正規化
# w = np.round(preprocessing.minmax_scale(w), 3)
# Arc = np.round(preprocessing.minmax_scale(Arc), 3)

# Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)

# print("📐 正規化 WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))


# WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
# print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))


# # 歪んだサイコロを1000回振ってサンプルを得る
# # next_position = random.choices(BPLIST, k = 1, weights = w)
# # next_position = random.choices(BPLIST, k = 1, weights = Arc_INVERSE)
# # next_position = random.choices(BPLIST, k = 1, weights = WEIGHT_CROSS)
# # next_position = BPLIST[w.index(max(w))]
# next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]

# print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{next_position}\n==================================")