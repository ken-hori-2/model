import math
import random
# from this import d

# agent_s_Î¸.py ã®æ´çver.


class Agent():

    def __init__(self, max_theta):
        
        self.lost = False

        self.GOAL_REACH_EXP_VALUE = max_theta # 50 # % self.max_theta = 50

    def policy(self, action, index):

        print("\n----- ð¤ð agent policy -----")
        print("action : {}".format(action))
        choice = action[index[0]]
        
        return choice

    def index(self):
        
        print("\n----- â ï¸  Îsã®æå°ãæ½åº -----")
        minIndex = [i for i, x in enumerate(self.s_theta) if x == min(self.s_theta)]
        print("min index : {}".format(minIndex))
        if len(minIndex) > 1:
            print("Îsã®æå°ãè¤æ°åããã¾ãã")
            minIndex = [random.choice(minIndex)]
            print("ã©ã³ãã ã§ å°éç{} = {} ãé¸æãã¾ããã".format(minIndex, self.exp_value[minIndex[0]]))
        else:
            print("Îsã®æå°ãä¸ã¤ããã¾ãã")
        
        print("æå°ã¹ãã¬ã¹[min Îs] = {}".format(self.s_theta[minIndex[0]]))
        print("æå¤§å°éç[max exp] : {}".format(self.exp_value[minIndex[0]]))

        self.prev_index = minIndex[0]

        return minIndex

    def lost_value(self):

        print("\n----- â ï¸  è¿·ã£ãããå¤å¥ -----")
        if all(elem  < self.GOAL_REACH_EXP_VALUE for elem in self.exp_value): # 50% or all(elem  > 0.5 for elem in s_theta)
            self.lost = True
        else:
            self.lost = False

        print("lost : {}".format(self.lost))

        return self.lost, self.GOAL_REACH_EXP_VALUE


    
    
    

    def expected_theta(self, theta, back):
        print("\n----- â ï¸  æå¾å¤(Î¸)æ¨å® -----")
        print("Î¸  = {}Â°".format(theta))
        
        s_theta = []
        # [s_theta.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        [s_theta.append(round(theta[x] * 0.01, 2)) for x in range(len(theta))] # +0.1ããªãããver.
        print("ÎsÎ¸ = {}".format(s_theta))
        
        if not all(elem  <= 1 for elem in s_theta):
            
            minus_index = [i for i, x in enumerate(s_theta) if x > 1.0 ]
            print("MIN INDEX : {}".format(minus_index))
            if len(minus_index) > 1:
                print("Îsã®æå°ãè¤æ°åããã¾ãã")
                for x in range(len(minus_index)):
                    s_theta[minus_index[x]] = 1.0
            else:
                print("Îsã®æå°ãä¸ã¤ããã¾ãã")
                s_theta[minus_index[0]] = 1.0
            print("å¤æ´å¾ ÎsÎ¸ = {}".format(s_theta))
        
        if back:
            s_theta[self.prev_index] = 1.0 # ä¸åº¦é¸æããå ´æã¯é¸æãã¥ãããªã
            print("[back]ð å¤æ´å¾ ÎsÎ¸ = {}".format(s_theta))

        exp_theta = []
        [exp_theta.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))]
        print("E(Î¸):{}%".format(exp_theta))

        self.s_theta = s_theta
        self.exp_value = exp_theta

        return self.exp_value


def main():
    permission_explore_node = 1
    max_theta = 50

    print("Î¸max : {}Â°".format(max_theta))
    print("max æ¢ç´¢ç¯å²(ãã¹) : {}".format(permission_explore_node))

    print("\n------------START------------\n")
    agent = Agent(max_theta)

    action_list = ["A", "B", "C"]
    # theta = [60, 50, 20]
    theta_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Goal_d = 10

    theta_0 = [60, 30, 20] # 0.7, 0.4, 0.3
    # theta_2 = [50, 40, 120]
    theta = [80, 90, 100]

    # theta_list = [[60, 30, 20], [80, 90, 70], [60, 30, 20]]
    # # theta_list = [[40, 60, 70], [60, 50, 70], [40, 60, 70]]
    # # theta_list = [[40, 50, 60], [60, 70, 80], [40, 50, 60]]
    theta_list = [[50, 60, 70], [70, 80, 90], [50, 60, 70]]

    # first = False
    back = False

    

    for epoch in range(0, 3): # t-1 t t+1

        # theta = random.choices(theta_list, k = 3)
       
        print("\n========== ð {}steps ==========".format(epoch))

        # agent.expected_theta(theta)
        agent.expected_theta(theta_list[epoch], back)

        lost, goal_r_v = agent.lost_value()

        
        

        if not lost:
            Index = agent.index()
            action = agent.policy(action_list, Index)
            # print("index : {}".format(Index))
            print("choice : {}".format(action))
        else:
            print("agent is lost")

            print("next action : {}".format("BACKðð"))
            
            back = True

            print("ã´ã¼ã«å°éçã®è¨±å®¹åº¦ : {} %".format(goal_r_v))
            print("â Î¸max : {}Â°".format((1-(goal_r_v*0.01))*100))

            print("       max æ¢ç´¢ç¯å²(ãã¹) : {}".format(permission_explore_node))
            permission_explore_node += 1
            print("lostå¾ max æ¢ç´¢ç¯å²(ãã¹) : {}".format(permission_explore_node))

        

    

main()