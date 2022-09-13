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

    def __init__(self, NODELIST):
        
        self.agent_state = State()
        self.reset()

        self.NODELIST = NODELIST

        self.default_stress = 1

    @property
    def actions(self):
        return [Action.UP, Action.DOWN,
                Action.LEFT, Action.RIGHT]

    def reset(self):
        # self.agent_state = State(6, 2)
        self.agent_state = State(6, 0)
        return self.agent_state

    def _move(self, state, action, TRIGAR):

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

    def policy(self, state, TRIGAR):
        # return (self.actions)

        if TRIGAR:
            return (self.actions[1])
        else:
            return (self.actions[0])

def main():

    total_stress = 0
    TRIGAR = False

    NODELIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]


    env = Enviroment(NODELIST)
    
    agent = Agent(env)
    
    state = env.reset()

    state_history = []
    print(state)
    state_history.append(state)
    
    for i in range(20):
        print("---------------")

        # if not TRIGAR:
        #     print("not trigar")
        if not NODELIST[state.row][state.column] == 1:
                NODELIST[state.row][state.column] = random.randint(0, 1)

        # add
        if state.row == 2:
            NODELIST[state.row][state.column] = 0
        print(NODELIST[state.row][state.column])
        print(NODELIST)

        action = agent.policy(state, TRIGAR)
        next_state, stress = env._move(state, action, TRIGAR)
        prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
        state = next_state
        print(state)
        state_history.append(state)


        if NODELIST[state.row][state.column] > 0:
            print("🪧 NODE : ⭕️")
            # if NODELIST[prev_state.row][prev_state.column] > 0:
            if prev_state.row > state.row:
                state_history.append(state)
                state_history.append(state)
            
        else:
            print("🪧 NODE : ❌")
            # state_history.append(state)

        if total_stress + stress >= 0:
            total_stress += stress

        if total_stress >= 1:
            TRIGAR = True
            print("=================")
            print("FULL ! MAX! 🔙⛔️")
            print("=================")
            # print(f"🤖 State:{state}")
            state_history.append(state)
            # state_history.append(state)
            # continue

            # back_position = prev_state
        else:
            TRIGAR = False

        print(f"🤖 State:{state}")
        print(f"Total Stress:{total_stress}")

        # action = agent.policy(state)
        # next_state, stress = env._move(state, action, TRIGAR)
        # state = next_state
        # print(state)
        # state_history.append(state)
    

    
    print(state_history)

main()