from enum import Enum
import numpy as np

import random


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

    def reward_func(self, state, TRIGAR):
        # reward = self.default_reward
        done = False
        # print(f"state:{state}")

        # Check an attribute of next state.
        # attribute = self.grid[state.row][state.column]
        attribute = self.NODELIST[state.row]

        if TRIGAR:
            reward = 0 # -self.default_reward
            print("Δs max")
            done = True
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

    def policy(self, state):
        # return random.choice(self.actions)
        return (self.actions[0]) 


def main():
    NODELIST = [0,
                0,
                1,
                0,
                1,
                1]
    # Make grid environment.
    # grid = [
    #     [0, 0, 0, 1],
    #     [0, 9, 0, -1],
    #     [0, 0, 0, 0]
    # ]
    grid = [
        [0, 9, 0, 0],
        [0, 9, 0, 0],
        [0, 9, 9, 0],
        [0, 9, 0, 1],
        [0, 9, 9, 0],
        [0, 9, 0, 0]
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

        while not done:
            print(f"state:{state}")
            STATE_HISTORY.append(state)
            print(f"total stress:{total_reward}")
            

            action = agent.policy(state)
            next_state, reward, done = env.step(action, TRIGAR)
            # total_reward += reward
            
            
            
            # state = next_state
            # print(f"NODE:{state}")

            if total_reward >= 3:
                TRIGAR = True
                # 終了する時
                done = True
                # 終了する時
                print("Node未発見 ->")
                print("stressfull")
                
            else:
                print("stress:{}".format(total_reward))
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

                total_reward += reward

            # STATE_HISTORY.append(state)
            print("#################")
            
            # total_reward += reward
            
            
            state = next_state
        

        print("Episode {}: Agent gets {} stress.".format(i, total_reward))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
