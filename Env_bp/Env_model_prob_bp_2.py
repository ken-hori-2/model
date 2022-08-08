from enum import Enum
from tkinter import FIRST
import numpy as np
import random

# Enviroment_Edit.py の整理ver.
# Enviroment_edit_model.py の整理ver.

# 使っているアニメーション -> Env_anim_Edit.py


# ベースはEnv_model_prefer.py
# prefer(優先)は、stress -= 1 or stress = 0 することでその道を進みやすくしていた
# N = 1 が一つもないと BPlist = []だから、戻る場所がなくて、終了してしまう


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
        self.default_stress = 1 # -0.04

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

    def stress_func(self, state, TRIGAR, BRANCH):
       
        done = False

        # Check an attribute of next state.
        attribute = self.NODELIST[state.row][state.column]

        if TRIGAR:
            stress = -self.default_stress
        else:
            # if attribute == 1:
            #     # Get reward! and the game ends.
            #     stress = 0 # -1 # 0                              # ここが reward = None の原因 or grid の 1->0 で解決
            # elif attribute == 0:
            #     # Get damage! and the game ends.
            #     stress = self.default_stress
            if attribute > 0.0:
                # Get reward! and the game ends.
                stress = 0 # -1 # 0                              # ここが reward = None の原因 or grid の 1->0 で解決
            else:
                stress = self.default_stress


        return stress, done

    def reset(self):
        # Locate the agent at lower left corner.
        self.agent_state = State(self.row_length - 1, 0)
        return self.agent_state

    def step(self, action, TRIGAR, BRANCH):
        next_state, stress, done = self.transit(self.agent_state, action, TRIGAR, BRANCH)
        if next_state is not None:
            self.agent_state = next_state
        

        return next_state, stress, done

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
        stress, done = self.stress_func(next_state, TRIGAR, BRANCH)
        return next_state, stress, done




class Agent():

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state, TRIGAR, BRANCH, TRIGAR2):
        # return random.choice(self.actions)
        
        if TRIGAR2:
            # print("TRIGAR2 TRUE")
            return (self.actions[0])
        
        elif TRIGAR:
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

    # data = [round(0.1 * random.randint(0, 10), 2) for x in range(5)]
    # data = [round(0.1 * random.randint(1, 10), 2) for x in range(5)]
    w = [round(0.1 * random.randint(1, 10), 2) for x in range(5)]
    # print(f"data = {data}")
    # NODELIST = [
    #         [0, 0, 0, 1, 1, 1],
    #         [0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 1, 0, 0],
    #         [1, 1, 1, 1, 0, 0],
    #         [1, 0, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0, 0] # start
    # ]
    # 2D grid でゴールに辿り着くには、BPlistも分岐の数だけ増やす or 二次元にしないといけない

    # NODELIST = [
    #         [0      ],#, 0, 0, 1, 1, 1],
    #         [data[4]],#, 0, 0, 1, 0, 0],
    #         [data[3]],#, 0, 0, 1, 0, 0],
    #         [data[2]],#, 0, 1, 1, 0, 0],
    #         [data[1]],#, 0, 0, 0, 0, 0],
    #         [data[0]],#, 0, 0, 0, 0, 0],
    #         [0      ]#, 0, 0, 0, 0, 0] # start
    # ]
    NODELIST = [
            [0   ],
            [w[4]],
            [w[3]],
            [w[2]],
            [w[1]],
            [w[0]],
            [0   ]
    ]
    
    grid = [
        [0],#, 0, 0, 0, 0, 0],
        [0],#, 0, 0, 0, 0, 0],
        [0],#, 0, 0, 0, 0, 0],
        [0],#, 0, 0, 0, 0, 0],
        [0],#, 0, 0, 0, 0, 0],
        [0],#, 0, 0, 0, 0, 0],
        [0]#, 0, 0, 0, 0, 0]
    ]
    env = Environment(grid, NODELIST)
    agent = Agent(env)



    # コメントアウト0730 -> Stressfull += 1, Stressfull = 1


    # Try 10 game.
    for i in range(1):
        
        # Initialize position of agent.
        state = env.reset()

        ########## parameter ##########
        total_stress = 0
        stress = 0
        done = False
        STATE_HISTORY = []
        TRIGAR = False
        BPLIST = []
        COUNT = 0
        j = 1
        BRANCH = False
        save = 0
        save_trigar = False
        FIRST = True
        Stressfull = 1 #3
        BACK = False
        BACK2 = False
        bf = True
        TRIGAR2 = False
        ########## parameter ##########

        PROB = []
        
        print("\n----Init Pose----")
        print(f"State:{state}")
        STATE_HISTORY.append(state)
        print(f"Total Stress:{total_stress}")
        # print("-----------------")
        action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
        next_state, stress, done = env.step(action, TRIGAR, BRANCH)
        prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
        state = next_state

        # print("\n-----{}Steps-----".format(COUNT+1))

        while not done:

            print("\n-----{}Steps-----".format(COUNT+1))

            # action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
            # next_state, stress, done = env.step(action, TRIGAR, BRANCH)
            # prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            # state = next_state
            # print("BPLIST:{}".format(BPLIST))
            # print("PROB:{}".format(PROB))

            if TRIGAR2:
                if BACK2:
                    w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
                    # bf = False
                    # BACK = False
                    # prob = [5,4,3,2,1]
                    prob = [len(BPLIST)-x for x in range(len(BPLIST))]
                    # 2 つのリストの要素同士の演算
                    w3 = [round(x/y, 3) for x,y in zip(w,prob)]
                    # 歪んだサイコロを1000回振ってサンプルを得る
                    next_position = random.choices(BPLIST, k = 1, weights = w)
                    BACK2 = False
                    # print(f"🤖State:{state}")
                # print(f"State:{state}, next position:{next_position[0]}")
                # print(f"NEXT POSITION:{next_position[0]}")
                # print("BPLIST:{}".format(BPLIST))

                # print("PROB(arc)  :{}".format(prob))
                if int(state.row) < int(next_position[0].row):
                    # print("\ntest2222222!\n")
                    TRIGAR2 = False
                    # TRIGAR = True
                    # print(f"🤖State:{state}")
                    COUNT += 1
                    # コメントアウト0807 これがあると、空白のステップが print される
                    # continue

                # continue
                try:
                    # if state == BPLIST[-j]:
                    if state == next_position[0]:

                        # prob.remove(prob[prob.index(next_position[0][0])])
                        BPLIST.remove(next_position[0])
                        print("BPLIST(remove):{}".format(BPLIST))
                        # print(f"prob(remove):{prob}")
                        BACK2 =True


                        # print("NEXT BP:{}".format(BPLIST[-j]))
                        # print("NEXT BP:{}".format(next_position))
                        print("Arrive at BP (戻り終わりました。)")
                        print(f"🤖State:{state}")
                        STATE_HISTORY.append(state)
                        
                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress



                        COUNT += 1
                        # add0807
                        continue
                    # else:
                    #     # print("NEXT BP:{}".format(BPLIST[-j]))
                    #     print("NEXT BP:{}".format(next_position[0]))
                    #     print("On the way BACK")

                    #     # ストレスをマイナスにさせない為に追加
                    #     # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                    #     # probablity
                    #     if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                    #         if total_stress + stress >= 0:
                    #             total_stress += stress

                    # print("\n-----{}Steps-----".format(COUNT+1))
                except:
                    print("state:{}".format(state))
                    print("これ以上戻れません。 終了します。")
                    # ストレスをマイナスにさせない為に追加
                    # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                    # probablity
                    if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        if total_stress + stress >= 0:
                            total_stress += stress
                    break

                # action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
                # next_state, stress, done = env.step(action, TRIGAR, BRANCH)

                # continue

            # action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
            # next_state, stress, done = env.step(action, TRIGAR, BRANCH)
            # prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            # state = next_state

            # print("\n-----{}Steps-----".format(COUNT+1))

            if TRIGAR:
                if BACK or bf:
                    w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
                    bf = False
                    BACK = False
                    # prob = [5,4,3,2,1]
                    prob = [len(BPLIST)-x for x in range(len(BPLIST))]
                    # 2 つのリストの要素同士の演算
                    w3 = [round(x/y, 3) for x,y in zip(w,prob)]
                    # 歪んだサイコロを1000回振ってサンプルを得る
                    next_position = random.choices(BPLIST, k = 1, weights = w)
                print(f"⚠️ NEXT POSITION:{next_position[0]}")
                # print("BPLIST:{}".format(BPLIST))

                # print("PROB(arc)  :{}".format(prob)) コメントアウト0807





                
                # print(state.row, next_position.row)
                # print(f"State:{state}, next position:{next_position[0]}")
                # if state == next_position[0]:
                #     print("TEST")
                # print(type(int(state.row)))
                # print(type(int(next_position[0].row)))
                if int(state.row) > int(next_position[0].row):
                    # print("\ntest1111!\n")
                    TRIGAR2 = True
                    # state = prev_state
                    # print(f"🤖State:{state}")
                    # continue

                try:
                    # if state == BPLIST[-j]:
                    if state == next_position[0]:

                        # prob.remove(prob[prob.index(next_position[0][0])])
                        BPLIST.remove(next_position[0])
                        print("BPLIST(remove):{}".format(BPLIST))
                        # print(f"prob(remove):{prob}")
                        BACK =True


                        # print("NEXT BP:{}".format(BPLIST[-j]))
                        # print("NEXT BP:{}".format(next_position[0]))
                        print("Arrive at BP (戻り終わりました。)!!!!!!!!!!!!")
                        print(f"🤖State:{state}")
                        STATE_HISTORY.append(state)
                        
                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress

                        # if int(state.row) > int(next_position[0].row):
                        #     print("\ntest2222222!\n")
                        #     TRIGAR2 = True
                        #     print(f"🤖State:{state}")
                            # continue



                        COUNT += 1
                        # add0807 これがないと通り過ぎてしまう
                        continue

                        ###################
                        # コメントアウト0806
                        # if not BRANCH:
                        #     BRANCH = True
                        #     TRIGAR = False
                        # else:
                        #     j += 1
                            
                        #     if state.column == 0:
                        #         BRANCH = False
                        # コメントアウト0806
                        j += 1
                        # コメントアウト0806
                        ###################
                    # elif state > next_position[0]:
                    #     print("\ntest!\n")

                    # else:
                    #     # print("NEXT BP:{}".format(BPLIST[-j]))
                    #     print("NEXT BP:{}".format(next_position))
                    #     print("On the way BACK")

                    #     # ストレスをマイナスにさせない為に追加
                    #     # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                    #     # probablity
                    #     if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                    #         if total_stress + stress >= 0:
                    #             total_stress += stress
                except:
                    print("state:{}".format(state))
                    print("これ以上戻れません。 終了します。")
                    # ストレスをマイナスにさせない為に追加
                    # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                    # probablity
                    if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        if total_stress + stress >= 0:
                            total_stress += stress


                    break # ADD 0730 expansion 無しの場合は何回も繰り返さない
                    # 以下は繰り返す場合
                    # total_stress = 0
                    j = 1
                    # Stressfull += 1
                    TRIGAR = False
                    
                    # Edit 0729
                    BPLIST.clear() # 🌏これをするなら、State[5, 0] = 1にしないといけない　&& 以下の add0729 は消す

                    continue # State[6, 0]に戻るのを防ぐ
            else:
                # 🌏BPLIST start地点を追加 add0729
                # if FIRST:
                #     BPLIST.append(state)
                #     FIRST = False
                ###########################

                if not BRANCH:
                    
                    # if NODELIST[state.row][state.column] == 1:
                    if NODELIST[state.row][state.column] > 0.0:
                        
                        print("🪧NODE : ⭕️")
                        BPLIST.append(state)

                        PROB.append(NODELIST[state.row][state.column])
                        # PROB.append(round(0.1 * random.randint(1, 10), 2))


                        STATE_HISTORY.append(state)

                        #####################################
                        STATE_HISTORY.append(state) # add0726
                        #####################################
                        
                        # 一個前が1ならpopで削除
                        print("📂Storage {}".format(BPLIST))
                        length = len(BPLIST)

                        # コメントアウト 0806
                        # if length > 1:
                        #     # if NODELIST[state.row+1][state.column] == 1:
                        #     if NODELIST[state.row][state.column] > 0.0:
                        #         print("削除前 {}".format(BPLIST))
                        #         BPLIST.pop(-2)
                        #         print("削除後 {}".format(BPLIST))
                        # コメントアウト 0806

                    else: # elif NODELIST[state.row][state.column] == 0: 
                        print("🪧NODE : ❌")

                    print("Δs = {}".format(stress))
                    ##############################
                    # add 0730
                    if total_stress + stress >= 0:
                    ##############################
                        total_stress += stress

                    if total_stress >= Stressfull:
                        TRIGAR = True
                        print("=================")
                        print("FULL ! MAX! 🔙⛔️")
                        print("=================")
                        ##################################
                        STATE_HISTORY.append(state) # 0729
                        ##################################
                        COUNT += 1
                        continue # add 0807
                # else: # 分岐は使わないので一旦コメントアウト0807
                #     ##############################
                #     # add 0730
                #     if total_stress + stress >= 0:
                #     ##############################
                #         total_stress += stress
                #     print("Δs = {}".format(stress))

                #     if total_stress >= Stressfull:
                #         print("=================")
                #         print("FULL ! MAX! 🔙⛔️")
                #         print("=================")
                #         print("分岐終了")
                #         STATE_HISTORY.append(state)
                #         TRIGAR = True
                #     else:
                #         TRIGAR = False

                #         # if NODELIST[state.row][state.column] == 1:
                #         if NODELIST[state.row][state.column] > 0.0:
                #             print("🪧NODE : ⭕️")
                #             #####################################
                #             STATE_HISTORY.append(state) # add0726
                #             #####################################
                #             if BPLIST[-1].row == state.row:
                #                 BPLIST.append(state)

                #                 PROB.append(NODELIST[state.row][state.column])
                #                 # PROB.append(round(0.1 * random.randint(1, 10), 2))
                #             else:
                #                 length = len(BPLIST)
                #                 for test in range (length):
                #                     if BPLIST[(length-1)-test].row == state.row:
                #                         BPLIST.insert((length-1)-test+1,state)
                #                         save = (length -1) - test + 1
                #                         save_trigar = True
                #                         break

                #             print(f"📂Storage:{BPLIST}")
                #             STATE_HISTORY.append(state)
                            
                #             ############################
                #             # 分岐先は削除しなくてもいいかも#
                #             ############################
                #             # 一個前が1ならpopで削除
                #             length = len(BPLIST)

                #             # コメントアウト 0806
                #             # if length > 1:
                #             #     if not state.column-1 == 0:
                #             #         # if NODELIST[state.row][state.column-1] == 1:
                #             #         if NODELIST[state.row][state.column] > 0.0:
                #             #             print("Branch方向 削除前 {}".format(BPLIST))
                #             #             if save_trigar:
                #             #                 BPLIST.pop(-(length + 1 - save))
                #             #                 save_trigar = False
                #             #             else:
                #             #                 BPLIST.pop(-2)
                #             #             print("Branch方向 削除後 {}".format(BPLIST))
                #             # コメントアウト 0806
                            
                #         else: # elif NODELIST[state.row][state.column] == 0: 
                #             print("🪧NODE : ❌")
            
            # print(f"🌏🤖State:{state}")
            print(f"🤖State:{state}")
            STATE_HISTORY.append(state)
            print(f"Total Stress:{total_stress}")
            # print("-----------------")
            # print("\n-----{}Steps-----".format(COUNT+1))

            action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
            next_state, stress, done = env.step(action, TRIGAR, BRANCH)
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            
            COUNT += 1
            if COUNT > 30:
                break
            
        # print(f"data = {data}")
        print(f"w = {w}")
        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
