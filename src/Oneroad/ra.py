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
        self.agent_state = State(6, 2)
        # self.agent_state = State(6, 0)
        return self.agent_state

    def can_action_at(self, state):
        if self.grid[state.row][state.column] == 0:
            return True
        else:
            return False

    def _move(self, state, action, TRIGAR):
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")

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
                stress = 0 # -1 # 0                              # ここが reward = None の原因 or grid の 1->0 で解決
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

        # if TRIGAR:
        #     return (self.actions[1])
        # else:
        #     return (self.actions[0])
        return random.choice(self.actions)

    

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
    
    grid = [
        [0, 9, 0, 9, 0, 0],
        [0, 0, 0, 9, 0, 0],
        [0, 9, 0, 0, 0, 9],
        [0, 9, 0, 9, 0, 0],
        [0, 9, 0, 9, 9, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 9, 0, 9, 0, 0]
    ]


    env = Enviroment(grid, NODELIST)
    
    agent = Agent(env)
    
    state = env.reset()

    state_history = []
    print(state)
    state_history.append(state)

    # action = agent.policy(state, TRIGAR)
    # next_state, stress = env._move(state, action, TRIGAR)
    # prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
    # state = next_state
    # print(state)
    # state_history.append(state)
    
    for i in range(100): # 20):
        print("\n========== 🌟 {}steps ==========".format(i+1))
        print(f"🤖 State:{state}")

        try:
            action = agent.policy(state, TRIGAR)
            next_state, stress = env._move(state, action, TRIGAR)
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            print(state)
            state_history.append(state)
        except:
            print("エラーメッセージ")

        # print(f"🤖 next State:{state}")
        print(f"Total Stress:{total_stress}")

        
    print(state_history)

main()