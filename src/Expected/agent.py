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

        print("\n----- ð¤ð agent policy -----")
        # print("exp goal : {}".format(list))
        # print("index : {}".format(index))
        print("action : {}".format(action))
        # choice = list[index[0]]
        choice = action[index[0]]
        
        return choice

    def index(self):
        
        
        print("\n----- â ï¸  Îsã®æå°ãæ½åº -----")
        minIndex = [i for i, x in enumerate(self.s) if x == min(self.s)]

        print("MIN INDEX : {}".format(minIndex))
        if len(minIndex) > 1:
            print("Îsã®æå°ãè¤æ°åããã¾ãã")
            minIndex = [random.choice(minIndex)]
            print("ã©ã³ãã ã§ å°éç{} = {} ãé¸æãã¾ããã".format(minIndex, self.exp_value[minIndex[0]]))
        else:
            print("Îsã®æå°ãä¸ã¤ããã¾ãã")
        
        print("min Îs = {}".format(self.s[minIndex[0]]))
        print("max exp : {}".format(self.exp_value[minIndex[0]]))

        return minIndex

    def value(self, list):

        print("\n----- â ï¸  è¿·ã£ãããå¤å¥ -----")
        if all(elem  < 50 for elem in list):
            self.lost = True

        return self.lost


    def arrival_prob(self, theta):
        print("\n----- ð¤ð arrival prob -----")
        print("Î¸  = {}".format(theta))
        # for x in range(len(theta)):
        #     self.s.append(round(theta[x] * 0.01 + 0.1, 2))
        #     self.exp_value.append(round(1.0 - self.s[x], 2)*100)

        # add clear
        self.s.clear()
        self.exp_value.clear()
        [self.s.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        [self.exp_value.append(round(1.0 - self.s[x], 2)*100) for x in range(len(theta))]
        print("Îs = {}".format(self.s))

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
        print("\n========== ð {}steps ==========".format(epoch))
        # print("Î¸ : {}".format(theta))
        # Exp_Goal, Index = agent.arrival_prob(theta)
        Exp_Goal = agent.arrival_prob(theta)

        print("å°éç:{}%".format(Exp_Goal))

        lost = agent.value(Exp_Goal)
        print("lost : {}".format(lost))

        if not lost:
            Index = agent.index()
            action = agent.policy(action_list, Exp_Goal, Index)
            print("choice : {}".format(action))
        else:
            print("agent is lost")

        

    

main()