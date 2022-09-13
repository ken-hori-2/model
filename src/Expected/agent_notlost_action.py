import math
import random
from turtle import back
# from this import d

# agent_s_θ.py の整理ver.


class Agent():

    def __init__(self,state ,stressfull, action, maxtheta):
        self.state = state
        self.stressfull = stressfull
        self.actionlist = action
        self.back = False
        self.s = 0
        self.max_theta = maxtheta # 50
        self.node = [1, 1, 0, 1, 0]

    def policy(self, action, index):

        print("\n----- 🤖🌟 agent policy -----")
        print("action : {}".format(action))
        # print(index)
        choice = action[index] # choice = index
        # print("choice : {}".format(choice))

        # self.actionlist = action
        
        return choice

    def s_judge(self, stressfull): # , maxtheta):
        
        print("\n----- ⚠️  最終発見ノードから　探索範囲内か？ max:{}-----".format(stressfull))
        # print("Δs : {}".format(self.s))
        self.state += 1
        # print("🤖 state : {}".format(self.state))
        if self.node[self.state] == 1:
            print("🪧 NODE : ⭕️")
            # self.s -= 1  
        else:
            print("🪧 NODE : ❌")
            self.s += 1
        
        print("Δs : {}".format(self.s))
        
        if self.s >= stressfull:
            print("Δs max")
            index = self.actionlist.index("BACK") # index = self.actionlist[1]
            self.back = True
            # stressfull = self.s_max(stressfull)
        else:
            print("Δs 許容内")
            index = self.actionlist.index("GO") # index = self.actionlist[0]
            self.back = False
            # self.s += 1
            # self.state += 1
        
        return index, self.back, stressfull, self.max_theta, self.state

    def s_max(self, stressfull):
        print("\n----- ⚠️  BACK -----")
        
        self.back = True
        print("back : {}".format(self.back))
        print("BACK 🔙")
        # stressfull += 1
        # self.max_theta += 10
        if (self.s - 1) >= 0:
            self.s = -1 # 0
        print("state : {}".format(self.state))
        self.state -= 2
        print("state : {}".format(self.state))

        return stressfull, self.max_theta, self.state


def main():

    stressfull = 1
    maxtheta = 50
    state = 0
    
    print("max 探索範囲(マス) : {}".format(stressfull))
    
    print("\n------------START------------\n")
    action_list = ["GO", "BACK"]
    agent = Agent(state, stressfull, action_list, maxtheta)

    
    
    back = False

    print("🤖 state : {}".format(state))

    

    for epoch in range(0, 4): # 14): # t-1 t t+1
       
        print("\n========== 🌟 {}steps ==========".format(epoch))
        index, back, stressfull, maxtheta, state = agent.s_judge(stressfull)

        if back:
            print("BACK 🔙")
            stressfull, maxtheta, state = agent.s_max(stressfull)
        
        print("🤖 state : {}".format(state))
        
        action = agent.policy(action_list, index)
        print("choice : {}".format(action))

        
        # print("next max 探索範囲(マス) : {}".format(stressfull))
        print("next max θ(許容方向) : {}".format(maxtheta))

       

        

    

main()