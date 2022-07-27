from enum import Enum
from sre_constants import BRANCH
from tkinter import FIRST
import numpy as np

import random

from sympy import re


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        # return "<State: [{}, {}]>".format(self.row, self.column)
        return "[{}, {}]".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column


class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2


class Environment():

    def __init__(self, grid, NODELIST, move_prob=0.8):
        # grid is 2d-array. Its values are treated as an attribute.
        # Kinds of attribute is following.
        #  0: ordinary cell
        #  -1: damage cell (game end)
        #  1: reward cell (game end)
        #  9: block cell (can't locate agent)
        self.grid = grid
        self.agent_state = State()

        # Default reward is minus. Just like a poison swamp.
        # It means the agent has to reach the goal fast!
        self.default_reward = 1 # -0.04

        # Agent can move to a selected direction in move_prob.
        # It means the agent will move different direction
        # in (1 - move_prob).
        self.move_prob = move_prob
        self.reset()

        self.NODELIST = NODELIST
        self.BPLIST = []

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

    @property
    def states(self):
        states = []
        for row in range(self.row_length):
            for column in range(self.column_length):
                # Block cells are not included to the state.
                if self.grid[row][column] != 9:
                    states.append(State(row, column))
        return states

    def transit_func(self, state, action):
        transition_probs = {}
        if not self.can_action_at(state):
            # Already on the terminal cell.
            return transition_probs

        opposite_direction = Action(action.value * -1)

        for a in self.actions:
            prob = 0
            if a == action:
                prob = 1 # prob = self.move_prob
            elif a != opposite_direction:
                prob = 0 # prob = (1 - self.move_prob) / 2

            next_state = self._move(state, a)
            if next_state not in transition_probs:
                transition_probs[next_state] = prob
            else:
                transition_probs[next_state] += prob

        return transition_probs

    def can_action_at(self, state):
        if self.grid[state.row][state.column] == 0:
            return True
        else:
            return False

    def _move(self, state, action):
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.LEFT:
            next_state.column -= 1
        elif action == Action.RIGHT:
            next_state.column += 1

        # Check whether a state is out of the grid.
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            # print("test1")
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            # print("test2")

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            # print("test3")

        return next_state

    def reward_func(self, state, TRIGAR):
        # reward = self.default_reward
        done = False
        # print(f"state:{state}")

        # Check an attribute of next state.
        # attribute = self.grid[state.row][state.column]
        # attribute = self.NODELIST[state.row]
        attribute = self.NODELIST[state]

        if TRIGAR:
            reward = -self.default_reward
            print("Δs max")
            # done = True
        else:
            if attribute == 1:
                # Get reward! and the game ends.
                reward = 0 # 1                              # ここが reward = None の原因 or grid の 1->0 で解決
                # done = True
            elif attribute == 0:
                # Get damage! and the game ends.
                reward = self.default_reward # reward = -1
                # done = True
        
        return reward, done

    def reset(self):
        # Locate the agent at lower left corner.
        self.agent_state = State(self.row_length - 1, 0)
        return self.agent_state

    def step(self, action, TRIGAR):
        next_state, reward, done = self.transit(self.agent_state, action, TRIGAR)
        if next_state is not None:
            self.agent_state = next_state
        

        return next_state, reward, done

    def transit(self, state, action, TRIGAR):
        transition_probs = self.transit_func(state, action)
        if len(transition_probs) == 0:
            return None, None, True

        next_states = []
        probs = []
        for s in transition_probs:
            next_states.append(s)
            probs.append(transition_probs[s])

        next_state = np.random.choice(next_states, p=probs)
        reward, done = self.reward_func(next_state, TRIGAR)
        return next_state, reward, done




class Agent():

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state, TRIGAR, BRANCH):
        # return random.choice(self.actions)
        # if TRIGAR:
        #     return (self.actions[1])
        # else:
        #     return (self.actions[0])
        if TRIGAR:
            if BRANCH:
                print("BRANCH TRUE")
                return (self.actions[3])
            else:
                return (self.actions[1])
        elif not TRIGAR:
            if BRANCH:
                print("BRANCH TRUE2")
                return (self.actions[3])
            else:
                return (self.actions[0])
        # elif BRANCH:
        #     return (self.actions[2])
        


def main():
    # NODELIST = [0,
    #             0,
    #             1,
    #             0,
    #             1,
    #             1]
    # NODELIST = [0,
    #             1,
    #             0,
    #             1,
    #             1,
    #             0]
    NODELIST = [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    # Make grid environment.
    # grid = [
    #     [0, 0, 0, 1],
    #     [0, 9, 0, -1],
    #     [0, 0, 0, 0]
    # ]
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    env = Environment(grid, NODELIST)
    agent = Agent(env)






    # Try 10 game.
    for i in range(1):
        # Initialize position of agent.
        state = env.reset()
        total_reward = 0
        reward = 0
        done = False
        STATE_HISTORY = []
        TRIGAR = False
        
        BPLIST = []
        COUNT = 0
        select_next_bp = False
        down = False
        afterdown = False
        j = 1
        BRANCH = False
        FIRST = True
        branch_first = True
        BACK = False

        print(f"state:{state}")
        STATE_HISTORY.append(state)
        print(f"total stress:{total_reward}")
        print("#################")

        while not done:
            # print(f"state:{state}")
            # STATE_HISTORY.append(state)
            # print(f"total stress:{total_reward}")
            

            action = agent.policy(state, TRIGAR, BRANCH)
            next_state, reward, done = env.step(action, TRIGAR)
            # total_reward += reward
            
            state = next_state # comment out 0726
            
            
            
            # state = next_state
            # print(f"NODE:{state}")

            # if BRANCH:
            #     total_reward += reward
            # else:


            if TRIGAR:
                # pass
                print("BPLIST:{}".format(BPLIST))
                try:
                    if state == BPLIST[-j]:
                        print("NEXT BP:{}".format(BPLIST[-j]))
                        print("戻り終わりました。")
                        STATE_HISTORY.append(state)
                        # break
                        # TRIGAR = False
                        j += 1
                        total_reward += reward

                        BRANCH = True
                        # TRIGAR = False # 今はどっちでもいいかも
                        BACK = True
                    else:
                        print("On the way DOWN")
                except:
                    print("これ以上戻れません 終了します")
                    # break
                    total_reward = 0
                    j = 1
                    TRIGAR = False
                    BPLIST.clear()

                # if state.row == 5:
                #     print(type(state.row))
                #     print("終了")
                #     break
            else:
               if not BRANCH:
                if total_reward >= 3: #  and not TRIGAR: # :
                    # if FIRST:
                    #     TRIGAR = True     # back
                    #     FIRST = False
                    TRIGAR = True
                    # select_next_bp = True
                    # 終了する時
                    # done = True
                    # 終了する時
                    print("Node未発見 ->")
                    print("stressfull")
                    # total_reward += reward
                    
                else:
                    # TRIGAR = False
                    # print("stress:{}".format(total_reward))
                    print("NEXT STATE ROW :{}".format(state.row))
                    # print(NODELIST)
                    if NODELIST[state.row] == 1:
                        print("Node発見")
                        #########################
                        BPLIST.append(state)
                        # 一個前が1ならpopで削除
                        print("削除前 {}".format(BPLIST))
                        length = len(BPLIST)

                        # print(f"length:{length}")
                        if length > 1:
                            if NODELIST[state.row + 1] == 1:
                                BPLIST.pop(-2)
                                print("削除後 {}".format(BPLIST))
                        # print("storage  BPLIST:{}".format(BPLIST))
                        #########################
                        # state_history.append(state)                                       # comment out 0725
                    
                    else: # elif NODELIST[state.row] == 0: 
                        print("Node未発見")   
                        # total_reward += 1 # delta_s
                        # print("stress:{}".format(total_reward))

                    print("Δs = {}".format(reward))

                    total_reward += reward
               else:
                print("branch")

                # if branch_first:
                #     print("branch first")

                #     # total_reward = 0
                #     branch_first = False
                # else:
                total_reward += reward
                    # pass
                print(f"S:{total_reward}")
                if total_reward >= 3:
                    print("分岐終了")
                    break
                    


            # if select_next_bp:
            #     select_next_bp = False
            #     down = True
            #     print("select next bp")
                
                # try:
                #     next_bp = BPLIST[-j]
                #     print("[next bp : NODE {}]".format(next_bp[0]))
                # except:
                #     print("これ以上戻れません 終了します")
                    
                #     # done = True  # ループさせない時はこれを戻す # コメントアウト0725
                #     state = next_bp
                #     j = 1
                #     down = False
                #     total_reward = 0
                #     TRIGAR = False
                #     BPLIST.clear()
                #     print("state, j = {},{} BP list:{}".format(state, j, BPLIST))
                    
                #     print("[next bp : NODE {}]".format(next_bp))                   # tab 0725
                    
                #     done = True
                #     continue
                #     # return done, state, j, STATE_HISTORY                                # tab 0725
        

            # if down:
            #     down = False
            #     afterdown  = True
            #     print("On the way down")
            #     back_true = True
            #     while back_true:
            #         state.row += 1
            #         print("-----------")
            #         print("[NODE {}]".format(state))
            #         if state.row == next_bp:
            #             back_true = False
            #     print("-----------")
                
            #     # return done, state, j, state_history                                  # comment out 0725
            

            # if afterdown:
            #     afterdown = False
            #     # self.branch = True  コメントアウト 0724
            #     print("Afterdown Decision Making")
            #     select_next_bp = True
            #     j += 1
            
            # return done, state, j, STATE_HISTORY



            # STATE_HISTORY.append(state)
            print(f"state:{state}")
            STATE_HISTORY.append(state)
            print(f"total stress:{total_reward}")
            print("#################")
            
            # total_reward += reward
            
            
            # if not BACK:
            #     state = next_state
            # else:
            #     state = next_state



            COUNT += 1
            if COUNT > 30:
                break

            
        

        print("Episode {}: Agent gets {} stress.".format(i, total_reward))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
