import math
import random
from turtle import back
# from this import d

# agent_s_Î¸.py ã®æ´çver.


class Agent():

    def __init__(self, stressfull, action, maxtheta):
        self.stressfull = stressfull
        self.actionlist = action
        self.back = False
        self.s = 0
        self.max_theta = maxtheta # 50

    def policy(self, action, index):

        print("\n----- ð¤ð agent policy -----")
        print("action : {}".format(action))
        # print(index)
        choice = action[index] # choice = index
        # print("choice : {}".format(choice))

        # self.actionlist = action
        
        return choice

    def s_judge(self, stressfull): # , maxtheta):
        
        print("\n----- â ï¸  æçµçºè¦ãã¼ããããæ¢ç´¢ç¯å²åãï¼ max:{}-----".format(stressfull))
        print("Îs : {}".format(self.s))
        
        if self.s >= stressfull:
            print("Îs max")
            index = self.actionlist.index("BACK") # index = self.actionlist[1]
            self.back = True
            # stressfull = self.s_max(stressfull)
        else:
            print("Îs è¨±å®¹å")
            index = self.actionlist.index("GO") # index = self.actionlist[0]
            self.back = False
            self.s += 1
        
        return index, self.back, stressfull, self.max_theta

    def s_max(self, stressfull):
        print("\n----- â ï¸  BACK -----")
        
        self.back = True
        print("back : {}".format(self.back))
        print("BACK ð")
        stressfull += 1
        self.max_theta += 10
        self.s = 0

        return stressfull, self.max_theta


def main():

    stressfull = 1
    maxtheta = 50
    
    print("max æ¢ç´¢ç¯å²(ãã¹) : {}".format(stressfull))
    
    print("\n------------START------------\n")
    action_list = ["GO", "BACK"]
    agent = Agent(stressfull, action_list, maxtheta)

    
    
    back = False

    

    for epoch in range(0, 14): # t-1 t t+1
       
        print("\n========== ð {}steps ==========".format(epoch))
        index, back, stressfull, maxtheta = agent.s_judge(stressfull)

        if back:
            print("BACK ð")
            stressfull, maxtheta = agent.s_max(stressfull)
        
        action = agent.policy(action_list, index)
        print("choice : {}".format(action))

        
        # print("next max æ¢ç´¢ç¯å²(ãã¹) : {}".format(stressfull))
        print("next max Î¸(è¨±å®¹æ¹å) : {}".format(maxtheta))

       

        

    

main()