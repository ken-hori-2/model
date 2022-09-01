import math
from tkinter import RIGHT

from numpy import average
import random
import collections

# self.actions[0] -> i =  1 (↑)UP
# self.actions[1] -> i = -1 (↓)DOWN
# self.actions[2] -> i =  2 (←)LEFT
# self.actions[3] -> i = -2 (→)RIGHT

class Agent():

    def __init__(self, E):
        
        # self.actions[0] = UP
        # self.actions[1] = DOWN
        # self.actions[2] = LEFT
        # self.actions[3] = RIGHT
        self.E = E
        # print(self.E)

    def policy(self, ave, A):
        
        # value_max = max(V)
        # max_index = V.index(value_max)
        # next_action = A[max_index]

        maxIndex = [i for i, x in enumerate(ave) if x == max(ave)]
        print("MAX INDEX : {}".format(maxIndex))

        if len(maxIndex) > 1:
            print("平均価値の最大が複数個あります。")
            maxIndex = [random.choice(maxIndex)]
            print("ランダムで {} = {} を選択しました。".format(maxIndex, A[maxIndex[0]]))
        else:
            print("平均価値の最大が一つあります。")

        
        # next_action = A[ave.index(max(ave))]
        next_action = A[maxIndex[0]]
        print("次の行動 : {}, 平均価値 : {}".format(next_action, max(ave)))

        

        if next_action ==  1:
            NEXT = "UP"
        if next_action == -1:
            NEXT = "DOWN"
        if next_action ==  2:
            NEXT = "LEFT"
        if next_action == -2:
            NEXT = "RIGHT"
        
        return next_action, NEXT

    def value(self):

        V = [0]*4
        length = len(self.E[0])
        L = [length]*4
        for i in range(len(self.E[0])):
            if self.E[1][i] ==  1:
                V[0] += self.E[2][i]
            if self.E[1][i] == -1:
                V[1] += self.E[2][i]
            if self.E[1][i] ==  2:
                V[2] += self.E[2][i]
            if self.E[1][i] == -2:
                V[3] += self.E[2][i]

        ave = [V[x] / L[x] for x in range(len(V))]
        print("価値の平均:{}".format(ave))

        return V, ave


    def get_distance(x1, y1, x2, y2):
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    
    data = []

    X = [UP, DOWN, LEFT, RIGHT] # At-1
    A = [UP, DOWN, LEFT, RIGHT] # At
    R = [0, 1]
    # E = [
    #     [X[1], X[1], X[1], X[1], X[1], X[1], X[1], X[1]],
    #     [A[3], A[3], A[3], A[3], A[3], A[3], A[3], A[3]],
    #     [R[1], R[1], R[1], R[1], R[1], R[1], R[1], R[1]]
    #     ]
    # E = [
    #     [X[1], X[1], X[1], X[1], X[1], X[1], X[1], X[1]],
    #     [A[3], A[2], A[3], A[2], A[2], A[3], A[3], A[3]],
    #     [R[1], R[1], R[1], R[1], R[1], R[1], R[1], R[1]]
    #     ]

    # test
    A_test = [LEFT, RIGHT] # At
    E =[[], [], []]

    for i in range (50):
        E[0].append(X[1])
        E[1].append(random.choice(A_test))
        E[2].append(R[1])

    print(E[1])

    print("LEFT  : {}".format(E[1].count(2)))
    print("RIGHT : {}".format(E[1].count(-2)))
    # print("カウンター:{}".format(collections.Counter(E[1])))
    # Z = E(A == self.action[-1]) 今回は全部at-1 = ↓ のデータセット
    
    agent = Agent(E)
    # print(agent)

    V, ave = agent.value()
    print("V = {}".format(V))

    action, N = agent.policy(ave, A)

    print(action, N)
    
    data.append(action)

main()