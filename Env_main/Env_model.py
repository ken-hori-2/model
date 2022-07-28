from enum import Enum
from pickletools import stackslice
from sre_constants import BRANCH
from tkinter import FIRST
import numpy as np

import random

from sympy import re

# Enviroment_Edit.py の整理ver.
# Enviroment_edit_model.py の整理ver.


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        
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
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            

        return next_state

    def reward_func(self, state, TRIGAR, BRANCH):
        # reward = self.default_reward
        done = False

        # Check an attribute of next state.
        attribute = self.NODELIST[state.row][state.column]

        if TRIGAR:
            reward = -self.default_reward
            # print("Δs max")
            # done = True
        else:
            if attribute == 1:
                # Get reward! and the game ends.
                reward = 0                              # ここが reward = None の原因 or grid の 1->0 で解決
                
            elif attribute == 0:
                # Get damage! and the game ends.
                reward = self.default_reward
                

        
        return reward, done

    def reset(self):
        # Locate the agent at lower left corner.
        self.agent_state = State(self.row_length - 1, 0)
        return self.agent_state

    def step(self, action, TRIGAR, BRANCH):
        next_state, reward, done = self.transit(self.agent_state, action, TRIGAR, BRANCH)
        if next_state is not None:
            self.agent_state = next_state
        

        return next_state, reward, done

    def transit(self, state, action, TRIGAR, BRANCH):
        transition_probs = self.transit_func(state, action)
        if len(transition_probs) == 0:
            return None, None, True

        next_states = []
        probs = []
        for s in transition_probs:
            next_states.append(s)
            probs.append(transition_probs[s])

        next_state = np.random.choice(next_states, p=probs)
        reward, done = self.reward_func(next_state, TRIGAR, BRANCH)
        return next_state, reward, done




class Agent():

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state, TRIGAR, BRANCH):
        # return random.choice(self.actions)
        
        if TRIGAR:
            if BRANCH:
                print("BRANCH TRUE left")
                return (self.actions[2])
            else:
                return (self.actions[1])
        elif not TRIGAR:
            if BRANCH:
                print("BRANCH TRUE right")
                return (self.actions[3])
            else:
                return (self.actions[0])
        


def main():
    NODELIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
    ]
    
    grid = [
        [0, 9, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0]
    ]
    env = Environment(grid, NODELIST)
    agent = Agent(env)






    # Try 10 game.
    for i in range(1):
        # Initialize position of agent.
        state = env.reset()

        ########## parameter ##########
        total_reward = 0
        reward = 0
        done = False
        STATE_HISTORY = []
        TRIGAR = False
        BPLIST = []
        COUNT = 0
        j = 1
        BRANCH = False
        save = 0
        save_trigar = False
        ########## parameter ##########
        
        print("----Init Pose----")
        print(f"state:{state}")
        STATE_HISTORY.append(state)
        print(f"total stress:{total_reward}")
        
        print("-----------------")

        while not done:
            

            action = agent.policy(state, TRIGAR, BRANCH)
            next_state, reward, done = env.step(action, TRIGAR, BRANCH)
            
            
            
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            

            if TRIGAR:
                
                print("BPLIST:{}".format(BPLIST))
                try:
                    if state == BPLIST[-j]:
                        print("NEXT BP:{}".format(BPLIST[-j]))
                        
                        print("Arrive at BP (戻り終わりました。)")
                        STATE_HISTORY.append(state)
                        ##################################
                        # STATE_HISTORY.append(state) # 0726
                        ##################################
                        
                        # ストレスをマイナスにさせない為に追加
                        
                        
                        if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                            
                            if total_reward + reward >= 0:
                                total_reward += reward

                        if not BRANCH:
                            BRANCH = True
                            TRIGAR = False # TRUEだと発火
                        else:
                            
                            j += 1

                            
                        
                            if state.column == 0:
                                BRANCH = False
                        
                        # BACK = True
                    else:
                        print("NEXT BP:{}".format(BPLIST[-j]))
                        print("On the way BACK")
                        # ストレスをマイナスにさせない為に追加
                        
                        if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                            if total_reward + reward >= 0:
                                total_reward += reward
                except:
                    
                    print("state:{}".format(state))
                    # STATE_HISTORY.append(state)
                    print("これ以上戻れません。 終了します。")
                    break
                    # 以下は繰り返す場合
                    total_reward = 0
                    j = 1
                    TRIGAR = False
                    BPLIST.clear()

                
            else:
                if not BRANCH:
                    
                    if NODELIST[state.row][state.column] == 1:
                        
                        print("NODE : ⭕️")
                        
                        BPLIST.append(state)
                        STATE_HISTORY.append(state)

                        #####################################
                        STATE_HISTORY.append(state) # add0726
                        #####################################
                        
                        # 一個前が1ならpopで削除
                        print("Storage {}".format(BPLIST))
                        length = len(BPLIST)

                        
                        if length > 1:
                            
                            if NODELIST[state.row+1][state.column] == 1:
                                print("削除前 {}".format(BPLIST))
                                BPLIST.pop(-2)
                                print("削除後 {}".format(BPLIST))

                            
                        
                        
                    
                    else: # elif NODELIST[state.row][state.column] == 0: 
                        
                        print("NODE : ❌")

                        

                    print("Δs = {}".format(reward))

                    total_reward += reward

                    
                    
                    if total_reward >= 3:
                        TRIGAR = True
                        
                        print("=================")
                        print("FULL ! MAX! 🔙⛔️")
                        
                        print("=================")
                        ##################################
                        STATE_HISTORY.append(state) # 0729
                        ##################################
                        
                else:
                    


                    total_reward += reward

                    print("Δs = {}".format(reward))
                    
                    
                    if total_reward >= 3:

                        print("=================")
                        print("FULL ! MAX! 🔙⛔️")
                        print("=================")
                        print("分岐終了")
                        STATE_HISTORY.append(state)
                        
                        
                        TRIGAR = True
                    
                    else:
                        TRIGAR = False
                        if NODELIST[state.row][state.column] == 1:
                            
                            print("NODE : ⭕️")

                            #####################################
                            STATE_HISTORY.append(state) # add0726
                            #####################################
                            
                            
                            if BPLIST[-1].row == state.row:
                                BPLIST.append(state)
                            else:
                                
                                length = len(BPLIST)
                                
                                for test in range (length):
                                    
                                    
                                    if BPLIST[(length-1)-test].row == state.row:
                                        
                                            BPLIST.insert((length-1)-test+1,state)
                                            
                                            save = (length -1) - test + 1
                                            save_trigar = True
                                            break


                                

                            
                            print(f"Storage:{BPLIST}")
                            STATE_HISTORY.append(state)
                            
                            ############################
                            # 分岐先は削除しなくてもいいかも#
                            ############################
                            # 一個前が1ならpopで削除
                            
                            
                            length = len(BPLIST)

                            if length > 1:

                                if not state.column-1 == 0:
                                    
                                    if NODELIST[state.row][state.column-1] == 1:
                                        
                                        print("Branch方向 削除前 {}".format(BPLIST))
                                        if save_trigar:
                                            
                                            BPLIST.pop(-(length + 1 - save))
                                            save_trigar = False
                                        else:
                                            BPLIST.pop(-2)
                                        print("Branch方向 削除後 {}".format(BPLIST))


                        else: # elif NODELIST[state.row][state.column] == 0: 
                            
                            print("NODE : ❌")
                    


            



            
            print(f"State:{state}")
            STATE_HISTORY.append(state)
            print(f"Total Stress:{total_reward}")
            
            print("-----------------")



            COUNT += 1
            if COUNT > 30:
                break

            
        

        print("Episode {}: Agent gets {} stress.".format(i, total_reward))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
