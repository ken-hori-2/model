from enum import Enum

import random
# test.py
# agent_Edit.py と同じ


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        
        return "[{}, {}]".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    # def __hash__(self):
    #     return hash((self.row, self.column))

    # def __eq__(self, other):
    #     return self.row == other.row and self.column == other.column
        
class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2

class Enviroment():

    def __init__(self):
        
        self.agent_state = State()
        self.reset()

    @property
    def actions(self):
        return [Action.UP, Action.DOWN,
                Action.LEFT, Action.RIGHT]

    def reset(self):
        self.agent_state = State(0, 0)
        return self.agent_state

    def _move(self, state, action):

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            # next_state.row -= 1
            next_state.row += 1
        elif action == Action.DOWN:
            next_state.row -= 1
        elif action == Action.LEFT:
            next_state.column += 1
        elif action == Action.RIGHT:
            next_state.column -= 1

        return next_state

class Agent():

    def __init__(self, env, E_0, E_1, E_2, E_3):
        self.actions = env.actions

        self.E_0 = E_0
        self.E_1 = E_1
        self.E_2 = E_2
        self.E_3 = E_3
        print("E_0[At-1, At, Rt]:{}".format(self.E_0))
        print("E_1[At-1, At, Rt]:{}".format(self.E_1))
        print("E_2[At-1, At, Rt]:{}".format(self.E_2))
        print("E_3[At-1, At, Rt]:{}".format(self.E_3))

        self.V_0_LIST = []
        self.V_1_LIST = []
        self.V_2_LIST = []
        self.V_3_LIST = []

    def policy(self, state, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3, prev_action):
        # return (self.actions)
        # return (self.actions[0])

        try:
            maxIndex_0 = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
            print("MAX INDEX_0 : {}".format(maxIndex_0))
            if len(maxIndex_0) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex_0 = [random.choice(maxIndex_0)]
                print("ランダムで {} = {} を選択しました。".format(maxIndex_0, A_0[maxIndex_0[0]]))
            else:
                print("平均価値の最大が一つあります。")
            next_action_0 = A_0[maxIndex_0[0]]
            print("次の行動 : {}, 平均価値 : {}".format(next_action_0, max(ave_0)))
        except:
            print("ERROR")
            next_action_0 = random.choice(A_0)
            print("ランダムで {} を選択しました。".format(next_action_0))

        
        try:
            maxIndex_1 = [i for i, x in enumerate(ave_1) if x == max(ave_1)]
            print("MAX INDEX_1 : {}".format(maxIndex_1))
            if len(maxIndex_1) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex_1 = [random.choice(maxIndex_1)]
                print("ランダムで {} = {} を選択しました。".format(maxIndex_1, A_1[maxIndex_1[0]]))
            else:
                print("平均価値の最大が一つあります。")
            next_action_1 = A_1[maxIndex_1[0]]
            print("次の行動 : {}, 平均価値 : {}".format(next_action_1, max(ave_1)))
        except:
            print("ERROR")
            next_action_1 = random.choice(A_1)
            print("ランダムで {} を選択しました。".format(next_action_1))

        
        try:
            maxIndex_2 = [i for i, x in enumerate(ave_2) if x == max(ave_2)]
            print("MAX INDEX_2 : {}".format(maxIndex_2))
            if len(maxIndex_2) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex_2 = [random.choice(maxIndex_2)]
                print("ランダムで {} = {} を選択しました。".format(maxIndex_2, A_2[maxIndex_2[0]]))
            else:
                print("平均価値の最大が一つあります。")
            next_action_2 = A_2[maxIndex_2[0]] # 1 or -1
            print("次の行動 : {}, 平均価値 : {}".format(next_action_2, max(ave_2)))
        except:
            print("ERROR")
            next_action_2 = random.choice(A_2)
            print("ランダムで {} を選択しました。".format(next_action_2))

        
        try:
            maxIndex_3 = [i for i, x in enumerate(ave_3) if x == max(ave_3)]
            print("MAX INDEX_3 : {}".format(maxIndex_3))
            if len(maxIndex_3) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex_3 = [random.choice(maxIndex_3)]
                print("ランダムで {} = {} を選択しました。".format(maxIndex_3, A_3[maxIndex_3[0]]))
            else:
                print("平均価値の最大が一つあります。")
            next_action_3 = A_3[maxIndex_3[0]] # 1 or -1
            print("次の行動 : {}, 平均価値 : {}".format(next_action_3, max(ave_3)))
        except:
            print("ERROR")
            next_action_3 = random.choice(A_3)
            print("ランダムで {} を選択しました。".format(next_action_3))
        

        

        
        
        # return next_action_0, next_action_1, next_action_2, next_action_3
        if prev_action == self.actions[2] or prev_action == self.actions[3]:
            if next_action_2 == self.actions[0] or next_action_3 == self.actions[0]:
                print("🌟{}".format(Action.UP))
                return (self.actions[0])

            if next_action_2 == self.actions[1] or next_action_3 == self.actions[1]:
                print("🌟{}".format(Action.DOWN))
                return (self.actions[1])

        if prev_action == self.actions[0] or prev_action == self.actions[1]:
            if next_action_0 == self.actions[2] or next_action_1 == self.actions[2]:
                print("🌟{}".format(Action.LEFT))
                return (self.actions[2])
            
            if next_action_0 == self.actions[3] or next_action_1 == self.actions[3]:
                print("🌟{}".format(Action.RIGHT))
                return (self.actions[3])
    
    def value(self):

        V_0 = [0]*2
        V_1 = [0]*2
        V_2 = [0]*2
        V_3 = [0]*2
        length_0 = len(self.E_0[0])
        length_1 = len(self.E_1[0])
        length_2 = len(self.E_2[0])
        length_3 = len(self.E_3[0])
        
        L_0 = [length_0]*2
        L_1 = [length_1]*2
        L_2 = [length_2]*2
        L_3 = [length_3]*2
        for i in range(len(self.E_0[0])):
            
            if self.E_0[1][i] ==  2:
                # V_0[2] += self.E_0[2][i]
                V_0[0] += self.E_0[2][i]
            if self.E_0[1][i] == -2:
                # V_0[3] += self.E_0[2][i]
                V_0[1] += self.E_0[2][i]

        for i in range(len(self.E_1[0])):
            
            if self.E_1[1][i] ==  2:
                # V_1[2] += self.E_1[2][i]
                V_1[0] += self.E_1[2][i]
            if self.E_1[1][i] == -2:
                # V_1[3] += self.E_1[2][i]
                V_1[1] += self.E_1[2][i]
        
        for i in range(len(self.E_2[0])):
            if self.E_2[1][i] ==  1:
                V_2[0] += self.E_2[2][i]
            if self.E_2[1][i] == -1:
                V_2[1] += self.E_2[2][i]
            

        for i in range(len(self.E_3[0])):
            if self.E_3[1][i] ==  1:
                V_3[0] += self.E_3[2][i]
            if self.E_3[1][i] == -1:
                V_3[1] += self.E_3[2][i]
            

        # print(" V_0[LEFT, RIGHT] :{}, L : {}".format(V_0, L_0))
        # print(" V_1[LEFT, RIGHT] :{}, L : {}".format(V_1, L_1))
        # print(" V_2[UP, DOWN] :{}, L : {}".format(V_2, L_2))
        # print(" V_3[UP, DOWN] :{}, L : {}".format(V_3, L_3))

        try:
            ave_0 = [V_0[x] / L_0[x] for x in range(len(V_0))]
        except:
            print("ERROR")
            ave_0 = V_0[0]
        print("価値 V_0 [LEFT, RIGHT] = {}".format(V_0))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_0))
        try:
            ave_1 = [V_1[x] / L_1[x] for x in range(len(V_1))]
        except:
            print("ERROR")
            ave_1 = V_1[0]
        print("価値 V_1 [LEFT, RIGHT] = {}".format(V_1))
        print("価値の平均[LEFT, RIGHT] : {}".format(ave_1))
        try:
            ave_2 = [V_2[x] / L_2[x] for x in range(len(V_2))]
        except:
            print("ERROR")
            ave_2 = V_2[0]
        print("価値 V_2 [UP, DOWN] = {}".format(V_2))
        print("価値の平均[UP, DOWN] : {}".format(ave_2))
        try:
            ave_3 = [V_3[x] / L_3[x] for x in range(len(V_3))]
        except:
            print("ERROR")
            ave_3 = V_3[0]
        print("価値 V_3 [UP, DOWN] = {}".format(V_3))
        print("価値の平均[UP, DOWN] : {}".format(ave_3))

        

        return ave_0, ave_1, ave_2, ave_3

def main():

    # param
    X = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT] # At-1
    A = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT] # At
    R = [0, 1]
    A_0 = [Action.LEFT, Action.RIGHT] # At
    
    A_1 = [Action.LEFT, Action.RIGHT] # At
    
    A_2 = [Action.UP, Action.DOWN] # At
    
    A_3 = [Action.UP, Action.DOWN] # At
    E_0 =[[], [], []]
    E_1 =[[], [], []]
    E_2 =[[], [], []]
    E_3 =[[], [], []]

    Z = [E_0, E_1, E_2, E_3]
    data_0 = []
    data_1 = []
    data_2 = []
    data_3 = []




    env = Enviroment()
    
    agent = Agent(env, E_0, E_1, E_2, E_3)
    
    state = env.reset()

    
    
    state_history = []
    # print(state)
    print("🤖State : {}".format(state))
    
    # for i in range(5):
    #     print("---------------")

    #     action = agent.policy(state, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3)
    #     next_state = env._move(state, action)
    #     state = next_state
    #     print(state)
    #     state_history.append(state)


    for epoch in range(1, 11):
        # for i in range (5*epoch):
        # for i in range (1):
        prev_action = random.choice(X) # At-1

        if prev_action == Action.UP: # X[0]: # UP
            E_0[0].append(prev_action)
            E_0[1].append(random.choice(A_0))
            # 今は次の行動で必ず発見できる前提(R = 1)
            E_0[2].append(R[0])
            # E_0[2].append(random.choice(R))
        if prev_action == Action.DOWN: # X[1]: # DOWN # defalt
            E_1[0].append(prev_action)
            E_1[1].append(random.choice(A_1)) # At-1 = DOWNの時の At
            # 今は次の行動で必ず発見できる前提(R = 1)
            E_1[2].append(R[0])
            # E_1[2].append(random.choice(R))
        if prev_action == Action.LEFT: # X[2]: # LEFT
            E_2[0].append(prev_action)
            E_2[1].append(random.choice(A_2))
            # 今は次の行動で必ず発見できる前提(R = 1)
            if E_2[1][-1] == A_2[0]: # UPならRt = 1
                print("⚡️ LEFT -> Rt = 1")
                # E_2[2].append(R[1])
                E_2[2].append(random.choice(R))
            else:
                E_2[2].append(R[0])
            
        if prev_action == Action.RIGHT: # X[3]: # RIGHT
            E_3[0].append(prev_action)
            E_3[1].append(random.choice(A_3))
            # 今は次の行動で必ず発見できる前提(R = 1)
            if E_3[1][-1] == A_3[0]: # UPならRt = 1
                print("⚡️ RIGHT -> Rt = 1")
                # E_3[2].append(R[1])
                E_3[2].append(random.choice(R))
            else:
                E_3[2].append(R[0])

        ave_0, ave_1, ave_2, ave_3 = agent.value()

        # action_0, action_1, action_2, action_3 = agent.policy(ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3)
        action = agent.policy(state, ave_0, ave_1, ave_2, ave_3, A_0, A_1, A_2, A_3, prev_action)
        next_state = env._move(state, action)
        state = next_state
        # print(state)
        print("🤖State : {}".format(state))
        state_history.append(state)

        data_0.append(action)
        # data_1.append(action_1)
        # data_2.append(action_2)
        # data_3.append(action_3)
    

    
    # print(state_history)
    print("🔑state history : {}\n".format(state_history))
    print("Data0={}".format(data_0))

main()