import random
import math

X = random.random()

print(X)

x2 = random.uniform(0.0, 1.0)
print(x2)
print(f"{x2:.2}")



# data = [random.randint(0, 10) for x in range(1, 10)]
data = [round(0.1 * random.randint(0, 10), 2) for x in range(10)]
print(data)



NODELIST = [
            [data[5], 0, 0, 1, 1, 1],
            [data[4], 0, 0, 1, 0, 0],
            [data[3], 0, 0, 1, 0, 0],
            [data[2], 1, 1, 1, 0, 0],
            [data[1], 0, 0, 0, 0, 0],
            [data[0], 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0] # start
    ]

print(NODELIST)


# newData = []
# for d in data:
#     if d % 2 == 0:
#         newData.append(d * 2)
# # 上記の場合には4行の実装ですが、リスト内包表記だと以下のように1行で記述することができます。
# newData = [d * 2 for d in data if d % 2 == 0]