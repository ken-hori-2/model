import math
import random
# from this import d

# agent_s_θ.py の整理ver.


class Agent():

    def __init__(self, max_theta):
        
        self.lost = False

        self.GOAL_REACH_EXP_VALUE = max_theta # 50 # % self.max_theta = 50

    def policy(self, action, index):

        print("\n----- 🤖🌟 agent policy -----")
        print("action : {}".format(action))
        choice = action[index[0]]
        
        return choice

    def index(self):
        
        print("\n----- ⚠️  Δsの最小を抽出 -----")
        minIndex = [i for i, x in enumerate(self.s_theta) if x == min(self.s_theta)]
        print("min index : {}".format(minIndex))
        if len(minIndex) > 1:
            print("Δsの最小が複数個あります。")
            minIndex = [random.choice(minIndex)]
            print("ランダムで 到達率{} = {} を選択しました。".format(minIndex, self.exp_value[minIndex[0]]))
        else:
            print("Δsの最小が一つあります。")
        
        print("最小ストレス[min Δs] = {}".format(self.s_theta[minIndex[0]]))
        print("最大到達率[max exp] : {}".format(self.exp_value[minIndex[0]]))

        self.prev_index = minIndex[0]

        return minIndex

    def lost_value(self):

        print("\n----- ⚠️  迷ったかを判別 -----")
        if all(elem  < self.GOAL_REACH_EXP_VALUE for elem in self.exp_value): # 50% or all(elem  > 0.5 for elem in s_theta)
            self.lost = True
        else:
            self.lost = False

        print("lost : {}".format(self.lost))

        return self.lost, self.GOAL_REACH_EXP_VALUE


    
    
    

    def expected_theta(self, theta, back):
        print("\n----- ⚠️  期待値(θ)推定 -----")
        print("θ  = {}°".format(theta))
        
        s_theta = []
        # [s_theta.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        [s_theta.append(round(theta[x] * 0.01, 2)) for x in range(len(theta))] # +0.1をなくしたver.
        print("Δsθ = {}".format(s_theta))
        
        if not all(elem  <= 1 for elem in s_theta):
            
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
        
        if back:
            s_theta[self.prev_index] = 1.0 # 一度選択した場所は選択しづらくなる
            print("[back]🔚 変更後 Δsθ = {}".format(s_theta))

        exp_theta = []
        [exp_theta.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(theta))]
        print("E(θ):{}%".format(exp_theta))

        self.s_theta = s_theta
        self.exp_value = exp_theta

        return self.exp_value


def main():
    permission_explore_node = 1
    max_theta = 50

    print("θmax : {}°".format(max_theta))
    print("max 探索範囲(マス) : {}".format(permission_explore_node))

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
       
        print("\n========== 🌟 {}steps ==========".format(epoch))

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

            print("next action : {}".format("BACK🔚🌟"))
            
            back = True

            print("ゴール到達率の許容度 : {} %".format(goal_r_v))
            print("≒ θmax : {}°".format((1-(goal_r_v*0.01))*100))

            print("       max 探索範囲(マス) : {}".format(permission_explore_node))
            permission_explore_node += 1
            print("lost後 max 探索範囲(マス) : {}".format(permission_explore_node))

        

    

main()