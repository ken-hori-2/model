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

        print("\n----- ๐ค๐ agent policy -----")
        print("action : {}".format(action))
        choice = action[index[0]]
        
        return choice

    def index(self, Exp_Goal):
        
        print("\n----- โ ๏ธ  ฮsใฎๆๅฐใๆฝๅบ -----")
        minIndex = [i for i, x in enumerate(self.s) if x == min(self.s)]

        print("MIN INDEX : {}".format(minIndex))
        if len(minIndex) > 1:
            print("ฮsใฎๆๅฐใ่คๆฐๅใใใพใใ")
            minIndex = [random.choice(minIndex)]
            print("ใฉใณใใ ใง ๅฐ้็{} = {} ใ้ธๆใใพใใใ".format(minIndex, Exp_Goal[minIndex[0]]))
        else:
            print("ฮsใฎๆๅฐใไธใคใใใพใใ")
        
        print("ๆๅฐในใใฌใน[min ฮs] = {}".format(self.s[minIndex[0]]))
        print("ๆๅคงๅฐ้็[max exp] : {}".format(Exp_Goal[minIndex[0]]))

        return minIndex

    def value(self, E_list):

        print("\n----- โ ๏ธ  ่ฟทใฃใใใๅคๅฅ -----")
        if all(elem  < 50 for elem in E_list):
            self.lost = True

        return self.lost


    def arrival_prob(self, theta, Exp_d):
        print("\n----- ๐ค๐ arrival prob -----")
        



        print("ๅฐ้็ E(d) : {}".format(Exp_d))
        print("ๅฐ้็ E(ฮธ):{}%".format(self.exp_value))
        E = []
        [E.append(round(self.exp_value[x] * Exp_d[x], 2)) for x in range(len(self.d))]
        print("ๅฐ้็ E = [E(ฮธ)*E(d)]: {}%".format(E))

        # add ฮs
        [self.s.append(round(self.s_distance[x] * self.s_theta[x], 2)) for x in range(len(self.s_distance))]
        print("๐ฮs = {}".format(self.s))

        
        # ๅฅๆก
        self.s.clear()
        [self.s.append(round(1.0 - E[x]*0.01, 2)) for x in range(len(self.s_distance))]
        print("๐๐ฮs = {}".format(self.s))




        return  E # self.exp_value

    def expected_theta(self, theta):
        print("\n----- โ ๏ธ  ๆๅพๅค(ฮธ)ๆจๅฎ -----")

        print("ฮธ  = {}".format(theta))
        # print("ๅฐ้็ E(d) : {}".format(Exp_d))
        # self.s.clear()
        s_theta = []
        self.exp_value.clear()
        [s_theta.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        # [self.exp_value.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))] # ไธใซ็งปๅ
        print("ฮsฮธ = {}".format(s_theta))

        # [s_theta[x] < 0 for x in range(len(theta))]
        if not all(elem  <= 1 for elem in s_theta):
            # print("test")
            minus_index = [i for i, x in enumerate(s_theta) if x > 1.0 ]

            print("MIN INDEX : {}".format(minus_index))
            if len(minus_index) > 1:
                print("ฮsใฎๆๅฐใ่คๆฐๅใใใพใใ")
                for x in range(len(minus_index)):
                    s_theta[minus_index[x]] = 1.0
                
            else:
                print("ฮsใฎๆๅฐใไธใคใใใพใใ")
                s_theta[minus_index[0]] = 1.0
                
            print("ๅคๆดๅพ ฮsฮธ = {}".format(s_theta))

        [self.exp_value.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))]

        print("E(ฮธ):{}%".format(self.exp_value))

        self.s_theta = s_theta


        return self.exp_value

    def distance(self, Arc, theta):

        print("\n----- โ ๏ธ  ้ฒใใ่ท้ขๆจๅฎ -----")
        print("Arc : {}".format(Arc))
        print("ฮธ  = {}".format(theta))

        test = []
        [test.append(round(math.cos(math.radians(theta[x])), 2)) for x in range(len(theta))]
        print("cosฮธ : {}".format(test))

        self.d.clear()
        # [self.d.append(round(Arc[x] * math.cos(math.radians(theta[x])), 2)) for x in range(len(theta))]
        [self.d.append(round(Arc[x] * test[x], 2)) for x in range(len(theta))]
        print("d = {}".format(self.d))
 
        

        return self.d

    def expected_d(self, Gd):

        print("\n----- โ ๏ธ  ๆๅพๅค(d)ๆจๅฎ -----")
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

        print("ฮsd = {}".format(sd))
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

        print("\n========== ๐ {}steps ==========".format(epoch))
        
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