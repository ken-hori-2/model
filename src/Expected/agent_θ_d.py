import math
from secrets import choice

from numpy import average
import random
import collections


class Agent():

    def __init__(self):
        self.s = []
        self.exp_value = []
        self.lost = False

        self.d = []

        self.s_distance = []
        self.s_theta = []
        # self.E = []
        


    def policy(self, action, list, index):

        print("\n----- 🤖🌟 agent policy -----")
        print("action : {}".format(action))
        choice = action[index[0]]
        
        return choice

    def index(self, Exp_Goal):
        
        print("\n----- ⚠️  Δsの最小を抽出 -----")
        minIndex = [i for i, x in enumerate(self.s) if x == min(self.s)]

        print("MIN INDEX : {}".format(minIndex))
        if len(minIndex) > 1:
            print("Δsの最小が複数個あります。")
            minIndex = [random.choice(minIndex)]
            print("ランダムで 到達率{} = {} を選択しました。".format(minIndex, Exp_Goal[minIndex[0]]))
        else:
            print("Δsの最小が一つあります。")
        
        print("最小ストレス[min Δs] = {}".format(self.s[minIndex[0]]))
        print("最大到達率[max exp] : {}".format(Exp_Goal[minIndex[0]]))

        return minIndex

    def value(self, E_list):

        print("\n----- ⚠️  迷ったかを判別 -----")
        if all(elem  < 50 for elem in E_list):
            self.lost = True

        return self.lost


    def arrival_prob(self, theta, Exp_d):
        print("\n----- 🤖🌟 arrival prob -----")
        



        print("到達率 E(d) : {}".format(Exp_d))
        print("到達率 E(θ):{}%".format(self.exp_value))
        E = []
        [E.append(round(self.exp_value[x] * Exp_d[x], 2)) for x in range(len(self.d))]
        print("到達率 E = [E(θ)*E(d)]: {}%".format(E))

        # add Δs
        [self.s.append(round(self.s_distance[x] * self.s_theta[x], 2)) for x in range(len(self.s_distance))]
        print("🌟Δs = {}".format(self.s))

        
        # 別案
        self.s.clear()
        [self.s.append(round(1.0 - E[x]*0.01, 2)) for x in range(len(self.s_distance))]
        print("🌟🌟Δs = {}".format(self.s))




        return  E # self.exp_value

    def expected_theta(self, theta):
        print("\n----- ⚠️  期待値(θ)推定 -----")

        print("θ  = {}".format(theta))
        # print("到達率 E(d) : {}".format(Exp_d))
        # self.s.clear()
        s_theta = []
        self.exp_value.clear()
        [s_theta.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        # [self.exp_value.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))] # 下に移動
        print("Δsθ = {}".format(s_theta))

        # [s_theta[x] < 0 for x in range(len(theta))]
        if not all(elem  <= 1 for elem in s_theta):
            # print("test")
            minus_index = [i for i, x in enumerate(s_theta) if x > 1.0 ]

            print("MIN INDEX : {}".format(minus_index))
            if len(minus_index) > 1:
                print("Δsの最小が複数個あります。")
                for x in range(len(minus_index)):
                    s_theta[minus_index[x]] = 1.0
                
            else:
                print("Δsの最小が一つあります。")
                s_theta[minus_index[0]] = 1.0
                
            print("変更後 Δsθ = {}".format(s_theta))

        [self.exp_value.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))]

        print("E(θ):{}%".format(self.exp_value))

        self.s_theta = s_theta


        return self.exp_value

    def distance(self, Arc, theta):

        print("\n----- ⚠️  進める距離推定 -----")
        print("Arc : {}".format(Arc))
        print("θ  = {}".format(theta))

        test = []
        [test.append(round(math.cos(math.radians(theta[x])), 2)) for x in range(len(theta))]
        print("cosθ : {}".format(test))

        self.d.clear()
        # [self.d.append(round(Arc[x] * math.cos(math.radians(theta[x])), 2)) for x in range(len(theta))]
        [self.d.append(round(Arc[x] * test[x], 2)) for x in range(len(theta))]
        print("d = {}".format(self.d))
 
        

        return self.d

    def expected_d(self, Gd):

        print("\n----- ⚠️  期待値(d)推定 -----")
        print("Goal distance = {}".format(Gd))
        d_rate = []
        [d_rate.append(self.d[x]/Gd) for x in range(len(self.d))]
        print("d_rate : d/Gd = {}".format(d_rate))

        

        sd = []
        for i in range(len(self.d)):
            if d_rate[i] <= 0.0:
                # sd.append(1.0 - abs(rate[i]))
                sd.append(abs(d_rate[i]))
            else:
                # sd.append(1.0 + abs(rate[i]))
                sd.append(-abs(d_rate[i]))

        print("Δsd = {}".format(sd))
        self.s_distance = sd

        Ed = []
        # for i in range(len(self.d)):
            #     Ed.append(1.0 - sd[i])
        [Ed.append(round(1.0 - sd[x], 2)) for x in range(len(self.d))]
        
        print("E(d) : {}%".format(Ed))

        return Ed





def main():

    print("\n------------START------------\n")
    agent = Agent()

    action_list = ["A", "B", "C"]
    theta = [60, 50, 20]
    theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    Goal_d = 10
    Arc_list = [2, 2, 2]

    for epoch in range(1, 2): # 4):

        theta = random.choices(theta_list, k = 3)
        theta = [60, 40, 40]
        theta = [50, 40, 120]
        theta = [80, 100, 100]
        Arc   = [2, 2, 2]
        Arc   = [5, 5, 5]

        print("\n========== 🌟 {}steps ==========".format(epoch))
        
        agent.distance(Arc, theta)
        Exp_distance = agent.expected_d(Goal_d)
        Exp_theta = agent.expected_theta(theta)
        
        Exp_Goal = agent.arrival_prob(Exp_theta, Exp_distance)

        lost = agent.value(Exp_Goal)
        print("lost : {}".format(lost))

        if not lost:
            Index = agent.index(Exp_Goal)
            action = agent.policy(action_list, Exp_Goal, Index)
            print("choice : {}".format(action))
        else:
            print("agent is lost")

        

    

main()