# モジュールのインポート
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# メイン実行部
# 試行回数nの初期化
n = int(input("試行回数nを入力してください:"))

fig = plt.figure()
ims = []

x = 0.0
y = 0.0
# グラフ描画の準備
xlist = [x]  # x座標
ylist = [y]  # y座標
# ランダムウォーク
for i in range(n):
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    xlist.append(x)
    ylist.append(y)
    im = plt.plot(xlist, ylist, marker='o', color = 'r')
    # im = plt.scatter(xlist, ylist, marker='o', color = 'r', alpha = 0.5)
    ims.append(im)
    # ims.append([ims])
# グラフの表示

ani = animation.ArtistAnimation(fig,ims,interval=300)
ani.save('test1.gif', writer='imagemagick')
plt.show()