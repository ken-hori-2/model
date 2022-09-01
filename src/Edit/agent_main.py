import math
from operator import length_hint
from tkinter import LEFT, RIGHT

from numpy import average
import random
import collections


# agent_add_Episode_Edit.py の整理ver.

# self.actions[0] -> i =  1 (↑)UP
# self.actions[1] -> i = -1 (↓)DOWN
# self.actions[2] -> i =  2 (←)LEFT
# self.actions[3] -> i = -2 (→)RIGHT

class Agent():

    def __init__(self):
        
        self.V_0_LIST = []
        self.V_1_LIST = []
        self.V_2_LIST = []
        self.V_3_LIST = []
        # self.V_LIST = []

        self.Episode_0 =[[], [], []]
        self.Episode_1 =[[], [], []]
        self.Episode_2 =[[], [], []]
        self.Episode_3 =[[], [], []]

        self.UP = 1
        self.DOWN = -1
        self.LEFT = 2
        self.RIGHT = -2
        self.A_0 = [self.LEFT, self.RIGHT] # At
        # A_1 = [DOWN, LEFT, RIGHT] # At
        self.A_1 = [self.LEFT, self.RIGHT] # At
        # A_2 = [UP, DOWN, LEFT] # At
        self.A_2 = [self.UP, self.DOWN] # At
        # A_3 = [UP, DOWN, RIGHT] # At
        self.A_3 = [self.UP, self.DOWN] # At


    def policy(self, prev_action, ave_0, ave_1, ave_2, ave_3): # _0, ave_1, ave_2, ave_3): # , A_0, A_1, A_2, A_3):

        print("\n----- 🤖🌟 agent policy -----")
        
        

        if prev_action == self.UP:
            print("🍏 At ①")
            try:
                print("\n----- ⚠️　各行動ごとの平均価値が一番大きい行動を選択-----")
                maxIndex = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
                print("\nMAX INDEX_0 : {}".format(maxIndex))
                if len(maxIndex) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex = [random.choice(maxIndex)]
                    print("ランダムで ave_0{} = {} を選択しました。".format(maxIndex, self.A_0[maxIndex[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_0 = A_0[maxIndex_0[0]]
                next_action = self.A_0[maxIndex[0]]
                print("At-1 = ⬆️  の時、次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(ave_0)))
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
                next_action = random.choice(self.A_0)
                print("ランダムで {} を選択しました。".format(next_action))

        elif prev_action == self.DOWN:
            print("🍏 At ②")
            try:
                maxIndex = [i for i, x in enumerate(ave_1) if x == max(ave_1)]
                print("\nMAX INDEX_1 : {}".format(maxIndex))
                if len(maxIndex) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex = [random.choice(maxIndex)]
                    print("ランダムで ave_1{} = {} を選択しました。".format(maxIndex, self.A_1[maxIndex[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_1 = A_1[maxIndex_1[0]]
                next_action = self.A_1[maxIndex[0]]
                print("At-1 = ⬇️  の時、次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(ave_1)))
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
                next_action = random.choice(self.A_1)
                print("ランダムで {} を選択しました。".format(next_action))

        elif prev_action == self.LEFT:
            print("🍏 At ③")
            try:
                maxIndex_2 = [i for i, x in enumerate(ave_2) if x == max(ave_2)]
                print("\nMAX INDEX_2 : {}".format(maxIndex_2))
                if len(maxIndex_2) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex_2 = [random.choice(maxIndex_2)]
                    print("ランダムで ave_2{} = {} を選択しました。".format(maxIndex_2, self.A_2[maxIndex_2[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_2 = A_2[maxIndex_2[0]] # 1 or -1
                next_action = self.A_2[maxIndex_2[0]] # 1 or -1
                print("At-1 = ⬅️  の時、次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(ave_2)))
            # except:
            except Exception as e:
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_2 = random.choice(A_2)
                next_action = random.choice(self.A_2)
                print("ランダムで {} を選択しました。".format(next_action))

        elif prev_action == self.RIGHT:
            print("🍏 At ④")
            try:
                maxIndex = [i for i, x in enumerate(ave_3) if x == max(ave_3)]
                print("\nMAX INDEX_3 : {}".format(maxIndex))
                if len(maxIndex) > 1:
                    print("平均価値の最大が複数個あります。")
                    maxIndex = [random.choice(maxIndex)]
                    print("ランダムで ave_3{} = {} を選択しました。".format(maxIndex, self.A_3[maxIndex[0]]))
                else:
                    print("平均価値の最大が一つあります。")
                # next_action_3 = A_3[maxIndex_3[0]] # 1 or -1
                next_action = self.A_3[maxIndex[0]] # 1 or -1
                print("At-1 = ⬅️  の時、次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(ave_3)))
            # except:
            except Exception as e:
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("ERROR")
                # next_action_3 = random.choice(A_3)
                next_action = random.choice(self.A_3)
                print("ランダムで {} を選択しました。".format(next_action))
        

        

        
        
        return next_action

    def value(self, prev_action):

        print("\n----- ⚠️  類似エピソード(At-1)ごとに価値計算-----\n")

        # ここで毎回リセットしないと前回の総和の計算結果を引き継いでしまう
        self.V_0 = [0]*2
        self.V_1 = [0]*2
        self.V_2 = [0]*2
        self.V_3 = [0]*2
        
        print("🌟 len = {}".format(len(self.Episode_2[0])))

        self.L_0 = [len(self.Episode_0[0])]*2
        self.L_1 = [len(self.Episode_1[0])]*2
        self.L_2 = [len(self.Episode_2[0])]*2
        self.L_3 = [len(self.Episode_3[0])]*2
        

        if prev_action == self.UP:
            for i in range(len(self.Episode_0[0])):
                
                if self.Episode_0[1][i] ==  self.LEFT: # At
                    # V_0[2] += self.E_0[2][i]
                    self.V_0[0] += self.Episode_0[2][i]
                if self.Episode_0[1][i] == self.RIGHT:
                    # V_0[3] += self.E_0[2][i]
                    self.V_0[1] += self.Episode_0[2][i]

        
        if prev_action == self.DOWN:
            for i in range(len(self.Episode_1[0])):
                if self.Episode_1[1][i] ==  self.LEFT:
                    # V_1[2] += self.E_1[2][i]
                    self.V_1[0] += self.Episode_1[2][i]
                if self.Episode_1[1][i] == self.RIGHT:
                    # V_1[3] += self.E_1[2][i]
                    self.V_1[1] += self.Episode_1[2][i]
        
        
        "======================================================================================================="
        if prev_action == self.LEFT: # self.Episode_2[0][i] == self.LEFT    # 戻る時の方向 (At-1)　類似エピソード抽出
            for i in range(len(self.Episode_2[0])):
                print("🌟 🌟 🌟 2")
                if self.Episode_2[1][i] ==  self.UP:                        # 類似エピソードの中の行動ごとに分類 (Episode_2 = prev_action = LEFT)
                    print("🌟 🌟 🌟 22")
                    self.V_2[0] += self.Episode_2[2][i]                     # その類似エピソードの時の行動の結果の価値を加算
                    # print("V = {}".format(self.V_2))
                if self.Episode_2[1][i] == self.DOWN:
                    self.V_2[1] += self.Episode_2[2][i]
        "======================================================================================================="
                

        if prev_action == self.RIGHT:
            for i in range(len(self.Episode_3[0])):
                print("🌟 🌟 🌟3")
                if self.Episode_3[1][i] ==  self.UP:
                    self.V_3[0] += self.Episode_3[2][i]
                if self.Episode_3[1][i] == self.DOWN:
                    self.V_3[1] += self.Episode_3[2][i]
            

        print("----- ⚠️　V = 各行動後に得た報酬の総和-----")
        print(" V_0[LEFT, RIGHT] :{}, L : {}".format(self.V_0, self.L_0))
        print(" V_1[LEFT, RIGHT] :{}, L : {}".format(self.V_1, self.L_1))
        print(" V_2[UP,   DOWN]  :{}, L : {}".format(self.V_2, self.L_2))
        print(" V_3[UP,   DOWN]  :{}, L : {}\n".format(self.V_3, self.L_3))

        

        try:
            ave_0 = [self.V_0[x] / self.L_0[x] for x in range(len(self.V_0))]
        except:
            ave_0 = self.V_0 # [0] # 0
        print("価値 V_0 [LEFT, RIGHT] = {}".format(self.V_0))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_0))
        try:
            ave_1 = [self.V_1[x] / self.L_1[x] for x in range(len(self.V_1))]
        except:
            ave_1 = self.V_1 # [0] # 0
        print("価値 V_1 [LEFT, RIGHT] = {}".format(self.V_1))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_1))
        try:
            ave_2 = [self.V_2[x] / self.L_2[x] for x in range(len(self.V_2))]
        except:
            ave_2 = self.V_2 # [0] # 0
        print("価値 V_2 [UP, DOWN] = {}".format(self.V_2))
        print("価値の平均[UP, DOWN] : {}".format(ave_2))
        try:
            ave_3 = [self.V_3[x] / self.L_3[x] for x in range(len(self.V_3))]
        except:
            ave_3 = self.V_3 # [0] # 0
        print("価値 V_3 [UP, DOWN] = {}".format(self.V_3))
        print("価値の平均[UP, DOWN] : {}".format(ave_3))

        

        return ave_0, ave_1, ave_2, ave_3


    def save_episode(self, prev_action, action):

        if prev_action == self.LEFT: # LEFT
            self.Episode_2[0].append(prev_action)
            self.Episode_2[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            
            if action == self.UP:
                print("⚡️ LEFT -> UP Rt = 1")
                self.Episode_2[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print("---------- 🔑 Episode2[⬅️ , ⬆️ ] : {}".format(self.Episode_2))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_2[2].append(0)

        if prev_action == self.RIGHT: # LEFT
            self.Episode_3[0].append(prev_action)
            self.Episode_3[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            
            if action == self.UP:
                print("⚡️ RIGHT -> UP Rt = 1")
                self.Episode_3[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print("---------- 🔑 Episode3[➡️ , ⬆️ ] : {}".format(self.Episode_3))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_3[2].append(0)

        if prev_action == self.UP: # LEFT
            self.Episode_0[0].append(prev_action)
            self.Episode_0[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            
            if action == self.UP:
                print("⚡️ UP -> UP Rt = 1")
                self.Episode_0[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print("---------- 🔑 Episode0[⬆️ , ⬆️ ] : {}".format(self.Episode_0))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_0[2].append(0)
        
        if prev_action == self.DOWN: # LEFT
            self.Episode_1[0].append(prev_action)
            self.Episode_1[1].append(action)                           # At-1 = LEFTの時の At(↑ ↓)
            
            if action == self.UP:
                print("⚡️ UP -> UP Rt = 1")
                self.Episode_1[2].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
                print("---------- 🔑 Episode1[⬇️ , ⬆️ ] : {}".format(self.Episode_1))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_1[2].append(0)

        return self.Episode_0, self.Episode_1, self.Episode_2, self.Episode_3




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    # X = [UP, DOWN, LEFT, RIGHT] # At-1
    # A = [UP, DOWN, LEFT, RIGHT] # At
    # R = [0, 1]

    # 目印を発見している限りは行動を継続している(つまり、未発見になって初めて方向を変える)と仮定すると、At-1で戻る時、その前のAt-2も戻る方向と同じ
    
    AVE_0_LIST = []
    AVE_1_LIST = []
    AVE_2_LIST = []
    AVE_3_LIST = []
    RESULT = []
    data = []

    V_LIST = []
    


    print("\n------------START------------\n")
    # コッチはデータをもとに行動がどのようになるかの実験
                
    agent = Agent()

    ################
    " add test "
    prev_action = 2 #1 # -1
    # 🍏ここを設定
    ################

    for epoch in range(1, 4): # 50):
        print("\n-----------{}steps------------\n".format(epoch))

        # prev_action = random.choice(X)
        
        ave_0, ave_1, ave_2, ave_3 = agent.value(prev_action)
        # ave = agent.value(prev_action)
        print("ave2:{}".format(ave_2))
        
        AVE_0_LIST.append(ave_0)
        AVE_1_LIST.append(ave_1)
        AVE_2_LIST.append(ave_2)
        AVE_3_LIST.append(ave_3)
        # V_LIST.append(ave)

        action = agent.policy(prev_action, ave_0, ave_1, ave_2, ave_3) #, A_0, A_1, A_2, A_3)
        # action = agent.policy(prev_action, ave)


        if action==  LEFT:
            NEXT = "LEFT  ⬅️"
            print("    At :-> {}".format(NEXT))
        if action == RIGHT:
            NEXT = "RIGHT ➡️"
            print("    At :-> {}".format(NEXT))  
        if action ==  UP:
            NEXT = "UP    ⬆️"
            print("    At :-> {}".format(NEXT))
        if action == DOWN:
            NEXT = "DOWN  ⬇️"
            print("    At :-> {}".format(NEXT))
        

        # print("\n---------- ⚠️ {}試行後の結果----------".format(5*epoch))
        print("\n---------- ⚠️  {}試行後の結果----------".format(epoch))
        print("過去のエピソードから、現時点では、At-1の時、Atを選択する")
        # Z = 類似エピソード
        
        "test0824"
        # Add Episode いつどの行動を取ったらどのくらい報酬が得られたか
        print("\n----- ⚠️  prev action = {}, action = {} -----".format(prev_action, action))
        
        print("🌟 action = {}".format(action))
        
        action = action
        
        Episode_0, Episode_1, Episode_2, Episode_3 = agent.save_episode(prev_action, action)



        # print("---------- 🔑 Episode_0 : {}----------".format(Episode_0))
        # print("---------- 🔑 Episode_1 : {}----------".format(Episode_1))
        # print("---------- 🔑 Episode_2 : {}----------".format(Episode_2))
        # print("---------- 🔑 Episode_3 : {}----------".format(Episode_3))
        

        data.append(action)
        
    print("\n---------- ⚠️  試行終了----------")
    
    print("平均価値[左からN回目]\n")
    print("V_0(⬅️ ➡️ ) : {}".format(AVE_0_LIST))
    print("V_1(⬅️ ➡️ ) : {}".format(AVE_1_LIST))
    print("V_2(⬆️ ⬇️ ) : {}".format(AVE_2_LIST))
    print("V_3(⬆️ ⬇️ ) : {}".format(AVE_3_LIST))
    # print("V : {}".format(V_LIST))

    # UPが一致しているSt
    if prev_action == 1:
        print("\nStが下から上に戻ってきた場合")
        print("UP -> LEFT  : {}".format(data.count(2)))
        print("UP -> RIGHT : {}".format(data.count(-2)))
        
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

    if prev_action == -2:
        print("\nStが左から右に戻ってきた場合")
        print("RIGHT -> UP    : {}".format(data.count(1)))
        print("RIGHT -> DOWN  : {}".format(data.count(-1)))
        RESULT.append(data.count(1))
        RESULT.append(data.count(-1))

    print("RESULT:{}".format(RESULT))

main()

# 一回も選択されていない方向があるとエラーが出る