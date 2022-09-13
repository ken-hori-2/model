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
        # pass


    def policy(self, action, list, index):

        print("\n----- 🤖🌟 agent policy -----")
        # print("exp goal : {}".format(list))
        # print("index : {}".format(index))
        print("action : {}".format(action))
        # choice = list[index[0]]
        choice = action[index[0]]
        
        return choice

    def index(self):
        
        
        print("\n----- ⚠️  Δsの最小を抽出 -----")
        minIndex = [i for i, x in enumerate(self.s) if x == min(self.s)]

        print("MIN INDEX : {}".format(minIndex))
        if len(minIndex) > 1:
            print("Δsの最小が複数個あります。")
            minIndex = [random.choice(minIndex)]
            print("ランダムで 到達率{} = {} を選択しました。".format(minIndex, self.exp_value[minIndex[0]]))
        else:
            print("Δsの最小が一つあります。")
        
        print("min Δs = {}".format(self.s[minIndex[0]]))
        print("max exp : {}".format(self.exp_value[minIndex[0]]))

        return minIndex

    def value(self, list):

        print("\n----- ⚠️  迷ったかを判別 -----")
        if all(elem  < 50 for elem in list):
            self.lost = True

        return self.lost


    def arrival_prob(self, theta):
        print("\n----- 🤖🌟 arrival prob -----")
        print("θ  = {}".format(theta))
        # for x in range(len(theta)):
        #     self.s.append(round(theta[x] * 0.01 + 0.1, 2))
        #     self.exp_value.append(round(1.0 - self.s[x], 2)*100)

        # add clear
        self.s.clear()
        self.exp_value.clear()
        [self.s.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        [self.exp_value.append(round(1.0 - self.s[x], 2)*100) for x in range(len(theta))]
        print("Δs = {}".format(self.s))

        return  self.exp_value




def main():

    print("\n------------START------------\n")
    agent = Agent()

    action_list = ["A", "B", "C"]
    theta = [60, 50, 20]
    # theta = [60, 50, 50]
    theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    for epoch in range(1, 4):

        theta = random.choices(theta_list, k = 3)
        # theta = [60, 40, 40]
        print("\n========== 🌟 {}steps ==========".format(epoch))
        # print("θ : {}".format(theta))
        # Exp_Goal, Index = agent.arrival_prob(theta)
        Exp_Goal = agent.arrival_prob(theta)

        print("到達率:{}%".format(Exp_Goal))

        lost = agent.value(Exp_Goal)
        print("lost : {}".format(lost))

        if not lost:
            Index = agent.index()
            action = agent.policy(action_list, Exp_Goal, Index)
            print("choice : {}".format(action))
        else:
            print("agent is lost")

        

    

main()