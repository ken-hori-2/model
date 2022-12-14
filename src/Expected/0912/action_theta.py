from enum import Enum
from random import random

import random
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

    def __init__(self, grid, NODELIST):
        
        self.agent_state = State()
        self.reset()

        self.grid = grid

        self.NODELIST = NODELIST

        self.default_stress = 1

    @property
    def row_length(self):
        return len(self.grid)

    @property
    def column_length(self):
        return len(self.grid[0])

    @property
    def actions(self):
        return [Action.UP, Action.DOWN,
                Action.LEFT, Action.RIGHT]

    def reset(self):
        # self.agent_state = State(6, 2)
        self.agent_state = State(6, 0)
        return self.agent_state

    # def can_action_at(self, state):
    #     if self.grid[state.row][state.column] == 0:
    #         return True
    #     else:
    #         return False

    def _move(self, state, action, TRIGAR):
        # if not self.can_action_at(state):
        #     raise Exception("Can't move from here!")

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
            # next_state.row += 1
        elif action == Action.DOWN:
            # next_state.row -= 1
            next_state.row += 1
        elif action == Action.LEFT:
            # next_state.column += 1
            next_state.column -= 1
        elif action == Action.RIGHT:
            # next_state.column -= 1
            next_state.column += 1

        stress = self.stress_func(next_state, TRIGAR)
        # return next_state, stress, done

        # Check whether a state is out of the grid.
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state

        return next_state, stress

    def stress_func(self, state, TRIGAR):
       
        done = False

        # Check an attribute of next state.
        attribute = self.NODELIST[state.row][state.column]

        if TRIGAR:
            stress = -self.default_stress
        else:
            
            if attribute > 0.0:
                # Get reward! and the game ends.
                stress = 0 # -1 # 0                              # ????????? reward = None ????????? or grid ??? 1->0 ?????????
            else:
                stress = self.default_stress


        return stress # , done

class Agent():

    def __init__(self, env):
        self.actions = env.actions
        self.GOAL_REACH_EXP_VALUE = 50 # max_theta # 50
        self.lost = False
        # self.prev_index = 0

    def policy(self, state, TRIGAR):
        # return (self.actions)

        if TRIGAR:
            return (self.actions[1])
        else:
            return (self.actions[0])

    def policy2(self, action, index):

        print("\n----- ???????? agent policy -----")
        print("action : {}".format(action))
        choice = action[index[0]]
        
        return choice

    def index(self):
        
        print("\n----- ??????  ??s?????????????????? -----")
        minIndex = [i for i, x in enumerate(self.s_theta) if x == min(self.s_theta)]
        print("min index : {}".format(minIndex))
        if len(minIndex) > 1:
            print("??s????????????????????????????????????")
            minIndex = [random.choice(minIndex)]
            print("??????????????? ?????????{} = {} ????????????????????????".format(minIndex, self.exp_value[minIndex[0]]))
        else:
            print("??s?????????????????????????????????")
        
        print("??????????????????[min ??s] = {}".format(self.s_theta[minIndex[0]]))
        print("???????????????[max exp] : {}".format(self.exp_value[minIndex[0]]))

        self.prev_index = minIndex[0]
        
        # self.s_theta[self.prev_index] = 1.0 # ???????????????????????????????????????????????????
        # print("[back]???? ????????? ??s?? = {}".format(self.s_theta))
        self.s_theta[self.prev_index] = 1.0 # ???????????????????????????????????????????????????
        print("[back]???? ????????? ??s?? = {}".format(self.s_theta))

        return minIndex

    def lost_value(self): # , theta_list):

        print("\n----- ??????  ????????????????????? -----")
        # print(theta_list)
        print("?????????????????????????????? : {} %".format(self.exp_value))
        if all(elem  < self.GOAL_REACH_EXP_VALUE for elem in self.exp_value): # 50% or all(elem  > 0.5 for elem in s_theta)
        # if all(elem  >= 50 for elem in theta_list): # 50% or all(elem  > 0.5 for elem in s_theta)
            self.lost = True
        else:
            self.lost = False

        print("lost : {}".format(self.lost))

        return self.lost # , self.GOAL_REACH_EXP_VALUE

    def cal(self, theta):
        s_theta = []
        [s_theta.append(round(theta[x] * 0.01, 2)) for x in range(len(theta))] # +0.1???????????????ver.
        print("??s?? = {}".format(s_theta))
        return s_theta

    def expected_theta(self, s_theta, lost): # , back):
        print("\n----- ????  ?????????(??)?????? -----")
        # print("??  = {}??".format(theta))
        
        # s_theta = []
        # # [s_theta.append(round(theta[x] * 0.01 + 0.1, 2)) for x in range(len(theta))]
        # [s_theta.append(round(theta[x] * 0.01, 2)) for x in range(len(theta))] # +0.1???????????????ver.
        print("??s?? = {}".format(s_theta))
        
        if not all(elem  <= 1 for elem in s_theta):
            
            minus_index = [i for i, x in enumerate(s_theta) if x > 1.0 ]
            print("MIN INDEX : {}".format(minus_index))
            if len(minus_index) > 1:
                print("??s????????????????????????????????????")
                for x in range(len(minus_index)):
                    s_theta[minus_index[x]] = 1.0
            else:
                print("??s?????????????????????????????????")
                s_theta[minus_index[0]] = 1.0
            print("????????? ??s?? = {}".format(s_theta))
        
        # if lost:
        #     s_theta[self.prev_index] = 1.0 # ???????????????????????????????????????????????????
        #     print("[back]???? ????????? ??s?? = {}".format(s_theta))

        exp_theta = []
        [exp_theta.append(round(1.0 - s_theta[x], 2)*100) for x in range(len(s_theta))]
        print("E(??):{}%".format(exp_theta))

        self.s_theta = s_theta
        self.exp_value = exp_theta

        return self.exp_value

def main():

    total_stress = 0
    TRIGAR = False
    theta_list = [0]*5 # [] # [0]*20
    lost = False

    NODELIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    THETALIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    STHETA = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]


    env = Enviroment(grid, NODELIST)
    
    agent = Agent(env)
    
    state = env.reset()

    state_history = []
    print(state)
    state_history.append(state)

    action = agent.policy(state, TRIGAR)
    next_state, stress = env._move(state, action, TRIGAR)
    prev_state = state # 1?????????????????????????????? -> ????????????????????????????????????
    state = next_state
    print(state)
    state_history.append(state)
    
    for i in range(15): # 20):
        print("---------------")
        print("\n========== ???? {}steps ==========".format(i+1))
        print(f"???? State:{state}")

        # if not NODELIST[state.row][state.column] == 1:
                # NODELIST[state.row][state.column] = random.randint(0, 1)
        if not NODELIST[state.row][state.column] == 0.5:
                NODELIST[state.row][state.column] = 0.5
                # theta_list.append([random.randint(0, 90) for i in range(2)]) # 3)])
                # theta_list[state.row] = ([random.randint(0, 90) for i in range(2)]) # 3)])
                THETALIST[state.row][state.column] = ([random.randint(0, 90) for i in range(2)]) # 3)])
                STHETA[state.row][state.column] = agent.cal(THETALIST[state.row][state.column])
                # agent.expected_theta(THETALIST[state.row][state.column])
        # print(NODELIST[state.row][state.column])
        # print(NODELIST)
        # print(theta_list)
        print(THETALIST)
        print(STHETA)

        # agent.expected_theta(theta_list[state.row]) # [i]) # , back)
        # agent.expected_theta(THETALIST[state.row][state.column], lost)
        agent.expected_theta(STHETA[state.row][state.column], lost)
        lost = agent.lost_value() # theta_list[i])

        # action = agent.policy(state, TRIGAR)
        # next_state, stress = env._move(state, action, TRIGAR)
        # prev_state = state # 1?????????????????????????????? -> ????????????????????????????????????
        # state = next_state
        # print(state)
        # state_history.append(state)


        # if NODELIST[state.row][state.column] >= 1: # > 0:
        #     print("???? NODE : ??????")
        #     if prev_state.row > state.row:
        #         state_history.append(state)
        #         state_history.append(state)
            
        # else:
        #     print("???? NODE : ???")

        # if total_stress + stress >= 0:
        #     total_stress += stress

        # if total_stress >= 1:
        if lost:
            TRIGAR = True
            print("=================")
            print("LOST ! ??????????")
            print("=================")
            state_history.append(state)
            # back_position = prev_state
        else:
            TRIGAR = False
            Index = agent.index()
            # action = agent.policy2(action_list, Index)
            # print("index : {}".format(Index))
            # print("choice : {}".format(action))

        try:
            action = agent.policy(state, TRIGAR)
            next_state, stress = env._move(state, action, TRIGAR)
            prev_state = state # 1?????????????????????????????? -> ????????????????????????????????????
            state = next_state
            print(state)
            state_history.append(state)
        except:
            print("????????????????????????")

        print(f"???? next State:{state}")
        print(f"Total Stress:{total_stress}")

        
    print(state_history)

main()