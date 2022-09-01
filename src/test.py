from enum import Enum
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

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        # return (self.actions)
        return (self.actions[0])

def main():
    env = Enviroment()
    
    agent = Agent(env)
    
    state = env.reset()

    state_history = []
    print(state)
    
    for i in range(5):
        print("---------------")

        action = agent.policy(state)
        next_state = env._move(state, action)
        state = next_state
        print(state)
        state_history.append(state)
    

    
    print(state_history)

main()