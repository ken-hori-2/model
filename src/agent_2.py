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

    def __init__(self, E_0, E_1, E_2, E_3):
        
        # self.actions[0] = UP
        # self.actions[1] = DOWN
        # self.actions[2] = LEFT
        # self.actions[3] = RIGHT
        self.E_0 = E_0
        self.E_1 = E_1
        self.E_2 = E_2
        self.E_3 = E_3
        print("E_0[At-1, At, Rt]:{}".format(self.E_0))
        print("E_1[At-1, At, Rt]:{}".format(self.E_1))
        print("E_2[At-1, At, Rt]:{}".format(self.E_2))
        print("E_3[At-1, At, Rt]:{}".format(self.E_3))

    def policy(self, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3):
        
        maxIndex_0 = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
        print("MAX INDEX_0 : {}".format(maxIndex_0))

        # print("A_0:{}".format(A_0))
        if len(maxIndex_0) > 1:
            print("平均価値の最大が複数個あります。")
            maxIndex_0 = [random.choice(maxIndex_0)]
            print("ランダムで {} = {} を選択しました。".format(maxIndex_0, A_0[maxIndex_0[0]]))
        else:
            print("平均価値の最大が一つあります。")
        next_action_0 = A_0[maxIndex_0[0]]
        print("次の行動 : {}, 平均価値 : {}".format(next_action_0, max(ave_0)))

        maxIndex_1 = [i for i, x in enumerate(ave_1) if x == max(ave_1)]
        print("MAX INDEX_1 : {}".format(maxIndex_1))
        if len(maxIndex_1) > 1:
            print("平均価値の最大が複数個あります。")
            maxIndex_1 = [random.choice(maxIndex_1)]
            print("ランダムで {} = {} を選択しました。".format(maxIndex_1, A_1[maxIndex_1[0]]))
        else:
            print("平均価値の最大が一つあります。")
        next_action_1 = A_1[maxIndex_1[0]]
        print("次の行動 : {}, 平均価値 : {}".format(next_action_1, max(ave_1)))

        maxIndex_2 = [i for i, x in enumerate(ave_2) if x == max(ave_2)]
        print("MAX INDEX_2 : {}".format(maxIndex_2))
        if len(maxIndex_2) > 1:
            print("平均価値の最大が複数個あります。")
            maxIndex_2 = [random.choice(maxIndex_2)]
            print("ランダムで {} = {} を選択しました。".format(maxIndex_2, A_2[maxIndex_2[0]]))
        else:
            print("平均価値の最大が一つあります。")
        next_action_2 = A_2[maxIndex_2[0]]
        print("次の行動 : {}, 平均価値 : {}".format(next_action_2, max(ave_2)))

        maxIndex_3 = [i for i, x in enumerate(ave_3) if x == max(ave_3)]
        print("MAX INDEX_3 : {}".format(maxIndex_3))
        if len(maxIndex_3) > 1:
            print("平均価値の最大が複数個あります。")
            maxIndex_3 = [random.choice(maxIndex_3)]
            print("ランダムで {} = {} を選択しました。".format(maxIndex_3, A_3[maxIndex_3[0]]))
        else:
            print("平均価値の最大が一つあります。")
        next_action_3 = A_3[maxIndex_3[0]]
        print("次の行動 : {}, 平均価値 : {}".format(next_action_3, max(ave_3)))

        

        
        
        return next_action_0, next_action_1, next_action_2, next_action_3 #, NEXT

    def value(self):

        # V_0 = [0]*4
        # V_1 = [0]*4
        # V_2 = [0]*4
        # V_3 = [0]*4
        V_0 = [0]*2
        V_1 = [0]*2
        V_2 = [0]*2
        V_3 = [0]*2
        length_0 = len(self.E_0[0])
        length_1 = len(self.E_1[0])
        length_2 = len(self.E_2[0])
        length_3 = len(self.E_3[0])
        # L_0 = [length_0]*4
        # L_1 = [length_1]*4
        # L_2 = [length_2]*4
        # L_3 = [length_3]*4
        L_0 = [length_0]*2
        L_1 = [length_1]*2
        L_2 = [length_2]*2
        L_3 = [length_3]*2
        for i in range(len(self.E_0[0])):
            # if self.E_0[1][i] ==  1:
            #     V_0[0] += self.E_0[2][i]
            # if self.E_0[1][i] == -1:
            #     V_0[1] += self.E_0[2][i]
            if self.E_0[1][i] ==  2:
                # V_0[2] += self.E_0[2][i]
                V_0[0] += self.E_0[2][i]
            if self.E_0[1][i] == -2:
                # V_0[3] += self.E_0[2][i]
                V_0[1] += self.E_0[2][i]

        for i in range(len(self.E_1[0])):
            # if self.E_1[1][i] ==  1:
            #     V_1[0] += self.E_1[2][i]
            # if self.E_1[1][i] == -1:
            #     V_1[1] += self.E_1[2][i]
            if self.E_1[1][i] ==  2:
                # V_1[2] += self.E_1[2][i]
                V_1[0] += self.E_1[2][i]
            if self.E_1[1][i] == -2:
                # V_1[3] += self.E_1[2][i]
                V_1[1] += self.E_1[2][i]
        
        for i in range(len(self.E_2[0])):
            if self.E_2[1][i] ==  1:
                V_2[0] += self.E_2[2][i]
            if self.E_2[1][i] == -1:
                V_2[1] += self.E_2[2][i]
            # if self.E_2[1][i] ==  2:
            #     V_2[2] += self.E_2[2][i]
            # if self.E_2[1][i] == -2:
            #     V_2[3] += self.E_2[2][i]

        for i in range(len(self.E_3[0])):
            if self.E_3[1][i] ==  1:
                V_3[0] += self.E_3[2][i]
            if self.E_3[1][i] == -1:
                V_3[1] += self.E_3[2][i]
            # if self.E_3[1][i] ==  2:
            #     V_3[2] += self.E_3[2][i]
            # if self.E_3[1][i] == -2:
            #     V_3[3] += self.E_3[2][i]

        print(" V_0[LEFT, RIGHT] :{}, L : {}".format(V_0, L_0))
        print(" V_1[LEFT, RIGHT] :{}, L : {}".format(V_1, L_1))
        print(" V_2[UP, DOWN] :{}, L : {}".format(V_2, L_2))
        print(" V_3[UP, DOWN] :{}, L : {}".format(V_3, L_3))

        try:
            ave_0 = [V_0[x] / L_0[x] for x in range(len(V_0))]
        except:
            ave_0 = V_0[0]
        print("価値 V_0 [LEFT, RIGHT] = {}".format(V_0))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_0))
        try:
            ave_1 = [V_1[x] / L_1[x] for x in range(len(V_1))]
        except:
            ave_1 = V_1[0]
        print("価値 V_1 [LEFT, RIGHT] = {}".format(V_1))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_1))
        try:
            ave_2 = [V_2[x] / L_2[x] for x in range(len(V_2))]
        except:
            ave_2 = V_2[0]
        print("価値 V_2 [UP, DOWN] = {}".format(V_2))
        print("価値の平均[UP, DOWN] : {}".format(ave_2))
        try:
            ave_3 = [V_3[x] / L_3[x] for x in range(len(V_3))]
        except:
            ave_3 = V_3[0]
        print("価値 V_3 [UP, DOWN] = {}".format(V_3))
        print("価値の平均[UP, DOWN] : {}".format(ave_3))

        return ave_0, ave_1, ave_2, ave_3 # V_0, V_1, V_2, V_3


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

    # 目印を発見している限りは行動を継続している(つまり、未発見になって初めて方向を変える)と仮定すると、At-1で戻る時、その前のAt-2も戻る方向と同じ
    # A_0 = [UP, LEFT, RIGHT] # At
    A_0 = [LEFT, RIGHT] # At
    # A_1 = [DOWN, LEFT, RIGHT] # At
    A_1 = [LEFT, RIGHT] # At
    # A_2 = [UP, DOWN, LEFT] # At
    A_2 = [UP, DOWN] # At
    # A_3 = [UP, DOWN, RIGHT] # At
    A_3 = [UP, DOWN] # At

    # E =[[], [], []]
    E_0 =[[], [], []]
    E_1 =[[], [], []]
    E_2 =[[], [], []]
    E_3 =[[], [], []]

    
    for i in range (50):
        prev_action = random.choice(X) # At-1

        if prev_action == X[0]: # UP
            E_0[0].append(prev_action)
            E_0[1].append(random.choice(A_0))
            # 今は次の行動で必ず発見できる前提(R = 1)
            # E_0[2].append(R[1])
            E_0[2].append(random.choice(R))
        if prev_action == X[1]: # DOWN # defalt
            E_1[0].append(prev_action)
            E_1[1].append(random.choice(A_1)) # At-1 = DOWNの時の At
            # 今は次の行動で必ず発見できる前提(R = 1)
            # E_1[2].append(R[1])
            E_1[2].append(random.choice(R))
        if prev_action == X[2]: # LEFT
            E_2[0].append(prev_action)
            E_2[1].append(random.choice(A_2))
            # 今は次の行動で必ず発見できる前提(R = 1)
            # E_2[2].append(R[1])
            E_2[2].append(random.choice(R))
        if prev_action == X[3]: # RIGHT
            E_3[0].append(prev_action)
            E_3[1].append(random.choice(A_3))
            # 今は次の行動で必ず発見できる前提(R = 1)
            # E_3[2].append(R[1])
            E_3[2].append(random.choice(R))

        
        

    # print(E_0[1])
    # print(E_1[1])
    # print(E_2[1])
    # print(E_3[1])

    # print("UP -> UP    : {}".format(E_0[1].count(1)))
    # print("UP -> DOWN  : {}".format(E_0[1].count(-1)))
    print("UP -> LEFT  : {}".format(E_0[1].count(2)))
    print("UP -> RIGHT : {}".format(E_0[1].count(-2)))
    
    # print("DOWN -> UP    : {}".format(E_1[1].count(1)))
    # print("DOWN -> DOWN  : {}".format(E_1[1].count(-1)))
    print("DOWN -> LEFT  : {}".format(E_1[1].count(2)))
    print("DOWN -> RIGHT : {}".format(E_1[1].count(-2)))


    print("LEFT -> UP    : {}".format(E_2[1].count(1)))
    print("LEFT-> DOWN  : {}".format(E_2[1].count(-1)))
    # print("DOWN -> LEFT  : {}".format(E_2[1].count(2)))
    # print("DOWN -> RIGHT : {}".format(E_2[1].count(-2)))

    print("RIGHT -> UP    : {}".format(E_3[1].count(1)))
    print("RIGHT -> DOWN  : {}".format(E_3[1].count(-1)))
    # print("DOWN -> LEFT  : {}".format(E_3[1].count(2)))
    # print("DOWN -> RIGHT : {}".format(E_3[1].count(-2)))
    
    # Z = E(prev_action == [UP,DOWN,LEFT,RIGHT]) 今回は全部at-1 = ↓ のデータセット
    # Z = [E_0, E_1, E_2, E_3]
    
    agent = Agent(E_0, E_1, E_2, E_3)
    # print(agent)

    ave_0, ave_1, ave_2, ave_3 = agent.value()
    # print("V = {}".format(V))

    action_0, action_1, action_2, action_3 = agent.policy(ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3)



    # if next_action_0 ==  1:
    #     NEXT_0 = "UP"
    # if next_action_0 == -1:
    #     NEXT_0 = "DOWN"
    if action_0==  2:
        NEXT_0 = "LEFT"
    if action_0 == -2:
        NEXT_0 = "RIGHT"
    # if next_action_1 ==  1:
    #     NEXT_1 = "UP"
    # if next_action_1 == -1:
    #     NEXT_1 = "DOWN"
    if action_1==  2:
        NEXT_1 = "LEFT"
    if action_1 == -2:
        NEXT_1 = "RIGHT"
    if action_2 ==  1:
        NEXT_2 = "UP"
    if action_2 == -1:
        NEXT_2 = "DOWN"
    # if next_action_2==  2:
    #     NEXT_2 = "LEFT"
    if action_2 == -2:
        NEXT_2 = "RIGHT"
    if action_3 ==  1:
        NEXT_3 = "UP"
    if action_3 == -1:
        NEXT_3 = "DOWN"
    # if next_action_3==  2:
    #     NEXT_3 = "LEFT"
    # if next_action_3 == -2:
    #     NEXT_3 = "RIGHT"

    print("\n最終結果")
    print("過去のエピソードから、現時点では、At-1の時、Atを選択する")
    # Z = 類似エピソード
    
    # print("[At-1, At] : UP -> {}".format(action_0))
    print("[At-1, At] : UP(Z=E_0) -> {}".format(NEXT_0))
    # print("[At-1, At] : DOWN -> {}".format(action_1))
    print("[At-1, At] : DOWN(Z=E_1) -> {}".format(NEXT_1))
    # print("[At-1, At] : LEFT -> {}".format(action_2))
    print("[At-1, At] : LEFT(Z=E_2) -> {}".format(NEXT_2))
    # print("[At-1, At] : RIGHT -> {}".format(action_3))
    print("[At-1, At] : RIGHT(Z=E_3) -> {}".format(NEXT_3))
    
    # data.append(action)

main()