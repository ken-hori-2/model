#データの生成
import numpy as np

# a = 1.5
# s = np.random.weibull(a, 1000000)
# print(type(s))
# x = np.arange(1,3, 1)
x = [0, 1, 2]
s = [0.9, 0.8, 0.5]

#可視化
import matplotlib.pyplot as plt
plt.bar(x,s)
# plt.bar(x, s, label = "IGNITION location", color="orange", ec="black")
plt.show()


#boxcox変換
from scipy.stats import boxcox
d = boxcox(s)
print(d)
plt.hist(d)

plt.show()