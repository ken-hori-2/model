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

    def __init__(self): # , E_0, E_1, E_2, E_3):
        
        # self.E_0 = E_0
        # self.E_1 = E_1
        # self.E_2 = E_2
        # self.E_3 = E_3
        # print("E_0[At-1, At, Rt]:{}".format(self.E_0))
        # print("E_1[At-1, At, Rt]:{}".format(self.E_1))
        # print("E_2[At-1, At, Rt]:{}".format(self.E_2))
        # print("E_3[At-1, At, Rt]:{}".format(self.E_3))

        self.V_0_LIST = []
        self.V_1_LIST = []
        self.V_2_LIST = []
        self.V_3_LIST = []

        self.Episode_0 =[[], [], []]
        self.Episode_1 =[[], [], []]
        self.Episode_2 =[[], [], []]
        self.Episode_3 =[[], [], []]

        self.UP = 1
        self.DOWN = -1
        self.LEFT = 2
        self.RIGHT = -2

    def policy(self, prev_action, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3):

        print("\n----- 🤖🌟 agent policy -----")
        
        

        if prev_action == 1:
            print("🍏 At ①")
            try:
                print("\n----- ⚠️　各行動ごとの平均価値が一番大きい行動を選択-----")
                maxIndex_0 = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
                print("\nMAX INDEX_0 : {}".format(maxIndex_0))
                if len(maxIndex_0) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex_0 = [random.choice(maxIndex_0)]
                    print("ランダムで ave_0{} = {} を選択しました。".format(maxIndex_0, A_0[maxIndex_0[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_0 = A_0[maxIndex_0[0]]
                next_action = A_0[maxIndex_0[0]]
                print("At-1 = ⬆️  の時、次の行動At : {}, 平均価値 : {}".format(next_action, max(ave_0)))
            # except:
            except Exception as e:
                print(ave_0)
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_0 = random.choice(A_0)
                next_action = random.choice(A_0)
                print("ランダムで {} を選択しました。".format(next_action))

        if prev_action == -1:
            print("🍏 At ②")
            try:
                maxIndex_1 = [i for i, x in enumerate(ave_1) if x == max(ave_1)]
                print("\nMAX INDEX_1 : {}".format(maxIndex_1))
                if len(maxIndex_1) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex_1 = [random.choice(maxIndex_1)]
                    print("ランダムで ave_1{} = {} を選択しました。".format(maxIndex_1, A_1[maxIndex_1[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_1 = A_1[maxIndex_1[0]]
                next_action = A_1[maxIndex_1[0]]
                print("At-1 = ⬇️  の時、次の行動At : {}, 平均価値 : {}".format(next_action, max(ave_1)))
            # except:
            except Exception as e:
                print(ave_1)
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_1 = random.choice(A_1)
                next_action = random.choice(A_1)
                print("ランダムで {} を選択しました。".format(next_action))

        if prev_action == 2:
            print("🍏 At ③")
            try:
                maxIndex_2 = [i for i, x in enumerate(ave_2) if x == max(ave_2)]
                print("\nMAX INDEX_2 : {}".format(maxIndex_2))
                if len(maxIndex_2) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex_2 = [random.choice(maxIndex_2)]
                    print("ランダムで ave_2{} = {} を選択しました。".format(maxIndex_2, A_2[maxIndex_2[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_2 = A_2[maxIndex_2[0]] # 1 or -1
                next_action = A_2[maxIndex_2[0]] # 1 or -1
                print("At-1 = ⬅️  の時、次の行動At : {}, 平均価値 : {}".format(next_action, max(ave_2)))
            # except:
            except Exception as e:
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_2 = random.choice(A_2)
                next_action = random.choice(A_2)
                print("ランダムで {} を選択しました。".format(next_action))

        if prev_action == -2:
            print("🍏 At ④")
            try:
                maxIndex_3 = [i for i, x in enumerate(ave_3) if x == max(ave_3)]
                print("\nMAX INDEX_3 : {}".format(maxIndex_3))
                if len(maxIndex_3) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex_3 = [random.choice(maxIndex_3)]
                    print("ランダムで ave_3{} = {} を選択しました。".format(maxIndex_3, A_3[maxIndex_3[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_3 = A_3[maxIndex_3[0]] # 1 or -1
                next_action = A_3[maxIndex_3[0]] # 1 or -1
                print("At-1 = ⬅️  の時、次の行動At : {}, 平均価値 : {}".format(next_action, max(ave_3)))
            # except:
            except Exception as e:
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_3 = random.choice(A_3)
                next_action = random.choice(A_3)
                print("ランダムで {} を選択しました。".format(next_action))
        

        

        
        
        return next_action # next_action_0, next_action_1, next_action_2, next_action_3 #, NEXT

    def value(self):

        print("\n----- ⚠️  類似エピソード(At-1)ごとに価値計算-----\n")

        V_0 = [0]*2
        V_1 = [0]*2
        V_2 = [0]*2
        V_3 = [0]*2
        length_0 = len(self.Episode_0[0])
        length_1 = len(self.Episode_1[0])
        length_2 = len(self.Episode_2[0])
        length_3 = len(self.Episode_3[0])
        
        L_0 = [length_0]*2
        L_1 = [length_1]*2
        L_2 = [length_2]*2
        L_3 = [length_3]*2


        print("🌟 len = {}".format(len(self.Episode_2[0])))
        # print(self.Episode_1)
        for i in range(len(self.Episode_0[0])):
            
            if self.Episode_0[1][i] ==  2:
                # V_0[2] += self.E_0[2][i]
                V_0[0] += self.Episode_0[2][i]
            if self.Episode_0[1][i] == -2:
                # V_0[3] += self.E_0[2][i]
                V_0[1] += self.Episode_0[2][i]

        
        for i in range(len(self.Episode_1[0])):
            
                if self.Episode_1[1][i] ==  2:
                    # V_1[2] += self.E_1[2][i]
                    V_1[0] += self.Episode_1[2][i]
                if self.Episode_1[1][i] == -2:
                    # V_1[3] += self.E_1[2][i]
                    V_1[1] += self.Episode_1[2][i]
        
        
        for i in range(len(self.Episode_2[0])):
                print("🌟 🌟 🌟2")
                if self.Episode_2[1][i] ==  1:
                    print("🌟 🌟 🌟 2")
                    V_2[0] += self.Episode_2[2][i]
                if self.Episode_2[1][i] == -1:
                    V_2[1] += self.Episode_2[2][i]
                # if self.E_2[1][i] ==  2:
                #     V_2[2] += self.E_2[2][i]
                # if self.E_2[1][i] == -2:
                #     V_2[3] += self.E_2[2][i]

        for i in range(len(self.Episode_3[0])):
            print("🌟 🌟 🌟3")
            if self.Episode_3[1][i] ==  1:
                V_3[0] += self.Episode_3[2][i]
            if self.Episode_3[1][i] == -1:
                V_3[1] += self.Episode_3[2][i]
            # if self.E_3[1][i] ==  2:
            #     V_3[2] += self.E_3[2][i]
            # if self.E_3[1][i] == -2:
            #     V_3[3] += self.E_3[2][i]

        print("----- ⚠️　V = 各行動後に得た報酬の総和-----")
        print(" V_0[LEFT, RIGHT] :{}, L : {}".format(V_0, L_0))
        print(" V_1[LEFT, RIGHT] :{}, L : {}".format(V_1, L_1))
        print(" V_2[UP,   DOWN]  :{}, L : {}".format(V_2, L_2))
        print(" V_3[UP,   DOWN]  :{}, L : {}\n".format(V_3, L_3))

        try:
            ave_0 = [V_0[x] / L_0[x] for x in range(len(V_0))]
        except:
            ave_0 = V_0 # [0] # 0
        print("価値 V_0 [LEFT, RIGHT] = {}".format(V_0))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_0))
        try:
            ave_1 = [V_1[x] / L_1[x] for x in range(len(V_1))]
        except:
            ave_1 = V_1 # [0] # 0
        print("価値 V_1 [LEFT, RIGHT] = {}".format(V_1))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_1))
        try:
            ave_2 = [V_2[x] / L_2[x] for x in range(len(V_2))]
        except:
            ave_2 = V_2 # [0] # 0
        print("価値 V_2 [UP, DOWN] = {}".format(V_2))
        print("価値の平均[UP, DOWN] : {}".format(ave_2))
        try:
            ave_3 = [V_3[x] / L_3[x] for x in range(len(V_3))]
        except:
            ave_3 = V_3 # [0] # 0
        print("価値 V_3 [UP, DOWN] = {}".format(V_3))
        print("価値の平均[UP, DOWN] : {}".format(ave_3))

        

        return ave_0, ave_1, ave_2, ave_3 # V_0, V_1, V_2, V_3


    # def get_distance(x1, y1, x2, y2):
    #     d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #     return d

    def save_episode(self, prev_action, action, reward):
        # print("関数 :{}".format(self.Episode_3))
        # if prev_action == self.UP: # UP
        #     self.Episode_0[0].append(prev_action)
        #     self.Episode_0[1].append(random.choice(A_0))                           # At-1 = UPの時の At(← →)
        #     self.Episode_0[2].append(R0)                                         # 今はUP以外は報酬0
            
        # if prev_action == self.DOWN: # DOWN # defalt
        #     self.Episode_1[0].append(prev_action)
        #     self.Episode_1[1].append(random.choice(A_1))                           # At-1 = DOWNの時の At(← →)
        #     self.Episode_1[2].append(R0)
            
        # if prev_action == self.LEFT: # LEFT
        #     self.Episode_2[0].append(prev_action)
        #     self.Episode_2[1].append(random.choice(A_2))                           # At-1 = LEFTの時の At(↑ ↓)
        #     if self.Episode_2[1][-1] == A_2[0]: # UPならRt = 1
        #         print("⚡️ LEFT -> UP Rt = 1")
        #         self.Episode_2[2].append(R1) # 今は次の行動で必ず発見できる前提(R = 1)
        #         # E_2[2].append(random.choice(R))
        #     else:
        #         self.Episode_2[2].append(R0)
        # if prev_action == self.RIGHT: # RIGHT
        #     self.Episode_3[0].append(prev_action)
        #     self.Episode_3[1].append(random.choice(A_3))                           # At-1 = RIGHTの時の At(↑ ↓)
        #     if self.Episode_3[1][-1] == A_3[0]: # UPならRt = 1
        #         print("⚡️ RIGHT -> UP Rt = 1")
        #         self.Episode_3[2].append(R1) # 今は次の行動で必ず発見できる前提(R = 1)
        #         # E_3[2].append(random.choice(R))
        #     else:
        #         self.Episode_3[2].append(R0)

        if prev_action == self.LEFT: # LEFT
            self.Episode_2[0].append(prev_action)
            self.Episode_2[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            # if self.Episode_2[1][-1] == self.UP: # A_2[0]: # UPならRt = 1
            if action == self.UP:
                print("⚡️ LEFT -> UP Rt = 1")
                self.Episode_2[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print(self.Episode_2)
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_2[2].append(0)

        if prev_action == self.RIGHT: # LEFT
            self.Episode_3[0].append(prev_action)
            self.Episode_3[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            # if self.Episode_2[1][-1] == self.UP: # A_2[0]: # UPならRt = 1
            if action == self.UP:
                print("⚡️ RIGHT -> UP Rt = 1")
                self.Episode_3[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print(self.Episode_3)
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_3[2].append(0)

        if prev_action == self.UP: # LEFT
            self.Episode_0[0].append(prev_action)
            self.Episode_0[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            # if self.Episode_2[1][-1] == self.UP: # A_2[0]: # UPならRt = 1
            if action == self.UP:
                print("⚡️ UP -> UP Rt = 1")
                self.Episode_0[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print(self.Episode_0)
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_0[2].append(0)
        
        if prev_action == self.DOWN: # LEFT
            self.Episode_1[0].append(prev_action)
            self.Episode_1[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            # if self.Episode_2[1][-1] == self.UP: # A_2[0]: # UPならRt = 1
            if action == self.UP:
                print("⚡️ UP -> UP Rt = 1")
                self.Episode_1[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print(self.Episode_1)
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_1[2].append(0)

        return self.Episode_0, self.Episode_1, self.Episode_2, self.Episode_3




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
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

    # data_0 = []
    # data_1 = []
    # data_2 = []
    # data_3 = []
    state = [0, 0]
    state_history = []
    V_0_LIST = []
    V_1_LIST = []
    V_2_LIST = []
    V_3_LIST = []
    RESULT = []

    DEMO = []

    data = []



    E_0 =[[], [], []]
    E_1 =[[], [], []]
    E_2 =[[], [], []]
    E_3 =[[], [], []]
    
    print("🤖State : {}".format(state))
    
    # for epoch in range(1, 101):
    # for epoch in range(1, 3):

    # データセットの生成
    # for i in range (5*epoch):

    "test0824"
    # agent = Agent(E_0, E_1, E_2, E_3)


    # print("5回分のデータを生成")
    # for i in range (10):
    #     # for i in range (1):
    #     prev_action = random.choice(X) # At-1

    #     E_0, E_1, E_2, E_3 = agent.save_episode(prev_action, X[0], X[1], X[2], X[3], A_0, A_1, A_2, A_3, R[0], R[1])


    # print("E_0[At-1, At, Rt] At-1 = ⬆️ : {}".format(E_0))
    # print("E_1[At-1, At, Rt] At-1 = ⬇️ : {}".format(E_1))
    # print("E_2[At-1, At, Rt] At-1 = ⬅️ : {}".format(E_2))
    # print("E_3[At-1, At, Rt] At-1 = ➡️ : {}".format(E_3))
    
    # print("\n-----------------------------\n")
    # print("上の回数をカウント (データセットは完全にランダムな行動)")
    
    # # print("UP -> UP    : {}".format(E_0[1].count(1)))
    # # print("UP -> DOWN  : {}".format(E_0[1].count(-1)))
    # print("E_0 At-1 = ⬆️")
    # print("     UP -> LEFT  : {}".format(E_0[1].count(2)))
    # print("     UP -> RIGHT : {}".format(E_0[1].count(-2)))
    # # print("DOWN -> UP    : {}".format(E_1[1].count(1)))
    # # print("DOWN -> DOWN  : {}".format(E_1[1].count(-1)))
    # print("E_1 At-1 = ⬇️")
    # print("     DOWN -> LEFT  : {}".format(E_1[1].count(2)))
    # print("     DOWN -> RIGHT : {}".format(E_1[1].count(-2)))

    # print("E_2 At-1 = ⬅️")
    # print("     LEFT -> UP    : {}".format(E_2[1].count(1)))
    # print("     LEFT-> DOWN  : {}".format(E_2[1].count(-1)))
    # # print("DOWN -> LEFT  : {}".format(E_2[1].count(2)))
    # # print("DOWN -> RIGHT : {}".format(E_2[1].count(-2)))
    # print("E_3 At-1 = ➡️")
    # print("     RIGHT -> UP    : {}".format(E_3[1].count(1)))
    # print("     RIGHT -> DOWN  : {}".format(E_3[1].count(-1)))
    # # print("DOWN -> LEFT  : {}".format(E_3[1].count(2)))
    # # print("DOWN -> RIGHT : {}".format(E_3[1].count(-2)))
    print("\n------------START------------\n")
    # コッチはデータをもとに行動がどのようになるかの実験
                
    agent = Agent()

    ################
    " add test "
    prev_action = 2 #1 # -1
    # 🍏ここを設定
    ################

    for epoch in range(1, 5): # 50):
        print("\n-----------{}steps------------\n".format(epoch))

        # prev_action = random.choice(X)
        
        
        # Z = E(prev_action == [UP,DOWN,LEFT,RIGHT]) 今回は全部at-1 = ↓ のデータセット
        # Z = [E_0, E_1, E_2, E_3]
        
        # agent = Agent() # E_0, E_1, E_2, E_3)
        # print(agent)

        ave_0, ave_1, ave_2, ave_3 = agent.value()
        # print("V = {}".format(V))
        V_0_LIST.append(ave_0)
        V_1_LIST.append(ave_1)
        V_2_LIST.append(ave_2)
        V_3_LIST.append(ave_3)

        

        # action_0, action_1, action_2, action_3 = agent.policy(prev_action, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3)
        action = agent.policy(prev_action, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3)


        if action==  2:
            NEXT = "LEFT  ⬅️"
            # state[1] -= 1
            print("    At :-> {}".format(NEXT))
        if action == -2:
            NEXT = "RIGHT ➡️"
            # state[1] += 1
            print("    At :-> {}".format(NEXT))
        
        # if action_1==  2:
        #     NEXT_1 = "LEFT  ⬅️"
        #     # state[1] -= 1
        # if action_1 == -2:
        #     NEXT_1 = "RIGHT ➡️"
        #     # state[1] += 1
        
        if action ==  1:
            NEXT = "UP    ⬆️"
            # state[0] += 1
            print("    At :-> {}".format(NEXT))
        if action == -1:
            NEXT = "DOWN  ⬇️"
            # state[0] -= 1
            print("    At :-> {}".format(NEXT))
        
        # if action_3 ==  1:
        #     NEXT_3 = "UP    ⬆️"
        #     # state[0] += 1
        # if action_3 == -1:
        #     NEXT_3 = "DOWN  ⬇️"
        #     # state[0] -= 1
        

        # print("\n---------- ⚠️ {}試行後の結果----------".format(5*epoch))
        print("\n---------- ⚠️  {}試行後の結果----------".format(epoch))
        print("過去のエピソードから、現時点では、At-1の時、Atを選択する")
        # Z = 類似エピソード
        
        # print("[At-1, At] : UP -> {}".format(action_0))
        # print("[At-1, At] : UP    ⬆️  -> {}".format(NEXT))

        # print("[At-1, At] : DOWN -> {}".format(action_1))
        # print("[At-1, At] : DOWN  ⬇️  -> {}".format(NEXT))

        # print("[At-1, At] : LEFT -> {}".format(action_2))
        # print("[At-1, At] : LEFT  ⬅️  -> {}".format(NEXT))

        # print("[At-1, At] : RIGHT -> {}".format(action_3))
        # print("[At-1, At] : RIGHT ➡️  -> {}".format(NEXT))




        "test0824"
        # Add Episode いつどの行動を取ったらどのくらい報酬が得られたか
        print("\n----- ⚠️  prev action = {}, action = {} -----".format(prev_action, action))
        # print("🌟 action = {}".format(action_2))
        # print("🌟 action = {}".format(action_3))
        # print("🌟 action = {}".format(action_0))
        print("🌟 action = {}".format(action))
        # prev_action = 2 # random.choice(X) # 今はランダムだが、いずれは上記で選択した行動
        # action = action_2 # random.choice(A)
        reward = random.choice(R)

        # prev_action = -2
        # action = action_3
        # prev_action = 1
        # action = action_0

        # prev_action = -1
        action = action
        # E_0, E_1, E_2, E_3 = agent.save_episode(prev_action, X[0], X[1], X[2], X[3], A_0, A_1, A_2, A_3, R[0], R[1])
        Episode_0, Episode_1, Episode_2, Episode_3 = agent.save_episode(prev_action, action, reward)



        # print("---------- 🔑 Episode_2 : {}----------".format(Episode_2))
        # print("---------- 🔑 Episode_3 : {}----------".format(Episode_3))
        # print("---------- 🔑 Episode_0 : {}----------".format(Episode_0))
        # print("---------- 🔑 Episode_1 : {}----------".format(Episode_1))






        
        data.append(action)
        # data_0.append(action_0)
        # data_1.append(action_1)
        # data_2.append(action_2)
        # data_3.append(action_3)

        # print("🤖State : {}".format(state))
        # state_history.append(state)

        # if prev_action == X[2]: # LEFT # [At-1, At] : LEFT -> {1:UP/-1:DOWN}
        #     if  action_2 == 1: # LEFT -> UP
        #         state[0] += 1
        #     elif action_2 == -1:
        #         state[0] -= 1
        
        # if prev_action == X[3]: # RIGHT # [At-1, At] : RIGHT -> {1:UP/-1:DOWN}
        #     if action_3 == 1: # RIGHT -> UP
        #         state[0] += 1
        #     elif action_2 == -1:
        #         state[0] -= 1

        # if prev_action == X[0]: # LEFT # [At-1, At] : LEFT -> {1:UP/-1:DOWN}
        #     if  action_0 == 2: # LEFT -> UP
        #         state[1] -= 1
        #     elif action_0 == -2:
        #         state[1] += 1
        # if prev_action == X[1]: # LEFT # [At-1, At] : LEFT -> {1:UP/-1:DOWN}
        #     if  action_1 == 2: # LEFT -> UP
        #         state[1] -= 1
        #     elif action_1 == -2:
        #         state[1] += 1
        # print("🤖State : {}".format(state))

        # state_history.append(state)
        # print("🔑state history : {}\n".format(state_history))

        # if state == [5, 0]:
        #     print("Goal🏁")
        #     break
        # # if state[0] > 3:
        # #     print("Failed❌")
        # #     break
        # if epoch >= 30:
        #     print("30ステップ以内に到達できませんでした🔚")
        #     break

        

    print("\n---------- ⚠️  試行終了----------")
    
    # print("Data0={}".format(data_0))
    # print("Data1={}".format(data_1))
    # print("Data2={}".format(data_2))
    # print("Data3={}".format(data_3))


    print("平均価値[左からN回目]\n")
    print("V_0(⬅️ ➡️ ) : {}".format(V_0_LIST))
    print("V_1(⬅️ ➡️ ) : {}".format(V_1_LIST))
    print("V_2(⬆️ ⬇️ ) : {}".format(V_2_LIST))
    print("V_3(⬆️ ⬇️ ) : {}".format(V_3_LIST))

    # UPが一致しているSt
    if prev_action == 1:
        print("\nStが下から上に戻ってきた場合")
        print("UP -> LEFT  : {}".format(data.count(2)))
        print("UP -> RIGHT : {}".format(data.count(-2)))
        # print("この状況では")
        RESULT.append(data.count(2))
        RESULT.append(data.count(-2))

    if prev_action == -1:
        print("\nStが上から下に戻ってきた場合")
        print("DOWN -> LEFT  : {}".format(data.count(2)))
        print("DOWN -> RIGHT : {}".format(data.count(-2)))
        RESULT.append(data.count(2))
        RESULT.append(data.count(-2))

    if prev_action == 2:
        print("\nStが右から左に戻ってきた場合")
        print("LEFT -> UP    : {}".format(data.count(1)))
        print("LEFT-> DOWN  : {}".format(data.count(-1)))
        RESULT.append(data.count(1))
        RESULT.append(data.count(-1))

    if prev_action == -1:
        print("\nStが左から右に戻ってきた場合")
        print("RIGHT -> UP    : {}".format(data.count(1)))
        print("RIGHT -> DOWN  : {}".format(data.count(-1)))
        RESULT.append(data.count(1))
        RESULT.append(data.count(-1))

    # print("\nAt-1 = -1")
    # print("DOWN -> LEFT  : {}".format(data_0.count(2)))
    # print("DOWN -> RIGHT : {}".format(data_0.count(-2)))

    # RESULT.append(data_0.count(2))
    # RESULT.append(data_0.count(-2))
    # RESULT.append(data_1.count(2))
    # RESULT.append(data_1.count(-2))
    # RESULT.append(data_2.count(1))
    # RESULT.append(data_2.count(-1))
    # RESULT.append(data_3.count(1))
    # RESULT.append(data_3.count(-1))
    

    print("RESULT:{}".format(RESULT))



    # print("\n-----🌟 今回のaction_2 -----")
    # print("action_2 process Data2 = {}".format(data_2))
    # print("LEFT -> UP    : {}".format(data_2.count(1)))
    # print("LEFT-> DOWN  : {}".format(data_2.count(-1)))
    # DEMO.append(data_2.count(1))
    # DEMO.append(data_2.count(-1))
    # print("DEMO : {}".format(DEMO))

    # print("\n-----🌟 今回のaction_3 -----")
    # print("action_3 process Data3 = {}".format(data_3))
    # print("RIGHT -> UP    : {}".format(data_3.count(1)))
    # print("RIGHT-> DOWN  : {}".format(data_3.count(-1)))
    # DEMO.append(data_3.count(1))
    # DEMO.append(data_3.count(-1))
    # print("DEMO : {}".format(DEMO))

    # print("\n-----🌟 今回のaction_0 -----")
    # print("action_0 process Data0 = {}".format(data_0))
    # print("UP -> LEFT    : {}".format(data_0.count(2)))
    # print("UP-> RIGHT  : {}".format(data_0.count(-2)))
    # DEMO.append(data_0.count(2))
    # DEMO.append(data_0.count(-2))
    # print("DEMO : {}".format(DEMO))

    # print("\n-----🌟 今回のaction_1 -----")
    # print("action_1 process Data1 = {}".format(data_1))
    # print("DOWN -> LEFT    : {}".format(data_1.count(2)))
    # print("DOWN-> RIGHT  : {}".format(data_1.count(-2)))
    # DEMO.append(data_1.count(2))
    # DEMO.append(data_1.count(-2))
    # print("DEMO : {}".format(DEMO))


main()

# 一回も選択されていない方向があるとエラーが出る