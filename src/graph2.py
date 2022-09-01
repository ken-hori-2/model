from turtle import color
import numpy as np
import matplotlib.pyplot as plt
 
# action = np.array([1,1, 2,2, 3,3, 4,4])
# num = np.array([5,8], [7,6], [12,1], [8,5])
# plt.bar(action, num)

# action = np.array([2, -2])
# num = np.array([5,8])
# plt.bar(action, num, color="orange")

# action = np.array([2, -2])
# num = np.array([7,6])
# plt.bar(action, num, color="blue")

# action = np.array([1, -1])
# num = np.array([12,1])
# plt.bar(action, num, color="green")

# action = np.array([1, -1])
# num = np.array([8,5])
# plt.bar(action, num, color="red")

# plt.show()

# action = np.array([1, -1])
x = [1, 2, 3, 4, 5, 6, 7, 8]
x = ["⇧ ⇦", "⇧ ⇨", "⇩ ⇦", "⇩ ⇨", "⇦ ⇧", "⇦ ⇩", "⇨ ⇧", "⇨ ⇩"]
# y = [2, -2, 2, -2, -2, 2] #([8,5],[6,0])
y = [3, 3, 3, 3, 6, 0, 4, 2]
y = [233, 267, 258, 242, 487, 13, 500, 0]
y = [254, 246, 254, 246, 498, 2, 496, 4]
y = [257, 243, 259, 241, 499, 1, 492, 8]
# plt.plot(num2, color="orange")
plt.bar(x, y, color="orange")

plt.show()

