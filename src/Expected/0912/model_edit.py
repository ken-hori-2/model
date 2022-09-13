from enum import Enum
from tkinter import FIRST
import numpy as np
import random

from sklearn import preprocessing

# ベースはEnv_model_prefer.py
# prefer(優先)は、stress -= 1 or stress = 0 することでその道を進みやすくしていた
# N = 1 が一つもないと BPlist = []だから、戻る場所がなくて、終了してしまう
# Env_bp/Env_model_prob_bp_2_Edit(match+cost).py の整理ver.
# model.py の整理ver.

# Env_bp/Edit のコピー


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

    
    w = [round(0.1 * random.randint(1, 10), 2) for x in range(5)]
    w = [1, 1, 1, 1, 1]
    # print(f"data = {data}")
    # w = [0.8, 0.6, 0.2, 0.9, 0.4]
    # NODELIST = [
    #         [0, 0, 0, 1, 1, 1],
    #         [1*0.4, 0, 0, 1, 0, 0],
    #         [1*0.9, 0, 0, 1, 0, 0],
    #         [1*0.2, 1, 1, 1, 0, 0],
    #         [1*0.6, 0, 0, 0, 0, 0],
    #         [1*0.8, 0, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0, 0] # start
    # ]
    NODELIST = [
            [0, 0, 0, 1, 1, 1],
            [1*0.4, 0, 0, 1, 0, 0],
            [1*0.8, 0, 0, 1, 0, 0],
            [1*0.2, 1, 1, 1, 0, 0],
            [1*0.6, 0, 0, 0, 0, 0],
            [1*0.9, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    # NODE = 1 の時に観測結果を格納する行列
    # Observation = [
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0, 0] # start
    # ]

    # 🔑今は観測されている前提の簡単なやつ
    Observation = [
            [0, 0, 0, 0, 0, 0],
            [0.4, 0, 0, 0, 0, 0],
            [0.9, 0, 0, 0, 0, 0],
            [0.2, 0, 0, 0, 0, 0],
            [0.6, 0, 0, 0, 0, 0],
            [0.8, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    print("Observation : {}".format(Observation))
    # 2D grid でゴールに辿り着くには、BPlistも分岐の数だけ増やす or 二次元にしないといけない

    
    
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
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
        
        FIRST = True
        Stressfull = 1 #3
        BACK = False
        BACK2 = False
        bf = True
        
        TRIGAR2 = False
        ########## parameter ##########

        PROB = []
        Arc = []
        OBS = []

        on_the_way = False
        
        print("\n----Init Pose----")
        print(f"State:{state}")
        STATE_HISTORY.append(state)
        print(f"Total Stress:{total_stress}")
        
        action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
        next_state, stress, done = env.step(action, TRIGAR, BRANCH)
        prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
        state = next_state



        while not done:

            print("\n-----{}Steps-----".format(COUNT+1))

            

            if TRIGAR2:
                if BACK2:
                    try:
                        # if bf2:
                        #     w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
                        #     bf2 = False
                        print(f"🥌 WEIGHT = {w}")
                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        
                        
                        
                        # 2 つのリストの要素同士の演算
                        ##### WEIGHT CROSS で割っているので要らない
                        Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
                        # print(f"1/Arc = {Arc_INVERSE}")
                        ##### WEIGHT CROSS で割っているので要らない

                        # add 0808 正規化
                        w = np.round(preprocessing.minmax_scale(w), 3)
                        Arc = np.round(preprocessing.minmax_scale(Arc), 3)

                        


                        Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
                        # print("📐正規化 w : {}, Arc : {}".format(w, Arc))
                        print("📐 正規化 WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))

                        # Arc = [0, 0]の時,Arc = [1, 1]に変更
                        if all(elem  == 0 for elem in Arc_INVERSE):
                            Arc_INVERSE = [1 for elem in Arc_INVERSE]
                            print("   Arc = [0, 0]の時, Arc_INVERSE : {}".format(Arc_INVERSE))
                        if all(elem  == 0 for elem in w):
                            w = [1 for elem in w]
                            print("   WEIGHT = [0, 0]の時, WEIGHT : {}".format(w))
                        
                        # WEIGHT_CROSS = [round(x/y, 3) for x,y in zip(w,Arc)]
                        WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
                        print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))
                        # 歪んだサイコロを1000回振ってサンプルを得る
                        # next_position = random.choices(BPLIST, k = 1, weights = w)
                        # next_position = random.choices(BPLIST, k = 1, weights = Arc_INVERSE)
                        # next_position = random.choices(BPLIST, k = 1, weights = WEIGHT_CROSS)
                        # next_position = BPLIST[w.index(max(w))]
                        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]
                        # print("next_position : {}".format(next_position))
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{next_position}\n==================================")
                        on_the_way = True
                        
                        

                        BACK2 = False
                    except:
                        print("ERROR!")
                        # STATE_HISTORY.append(state)
                        break
                    

                
                # if int(state.row) < int(next_position[0].row):
                if int(state.row) < int(next_position.row):
                    
                    TRIGAR2 = False
                    
                    COUNT += 1
                    
                try:
                    
                    # if state == next_position[0]:
                    if state == next_position:

                        
                        # bpindex = BPLIST.index(next_position[0])
                        bpindex = BPLIST.index(next_position)
                        
                        Arc = [(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
                        # print("Arc:{}".format(Arc))
                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        index = Arc.index(0)
                        Arc.pop(index)
                        # print("Arc:{}".format(Arc))
                        print("👟 Arc(remove 0[現在位置]):{}".format(Arc))

                        print("📂 Storage {}".format(BPLIST))
                        # BPLIST.remove(next_position[0])
                        BPLIST.remove(next_position)
                        
                        print("📂 Storage(remove) {}".format(BPLIST))

                        
                        BACK2 =True

                        
                        # w.pop(bpindex)
                        w = np.delete(w, bpindex)  # 削除できていない Arcは毎回入れ直しているからpopが使える
                        print("🥌 WEIGHT(remove):{}".format(w))
                        # Arc.pop(bpindex)


                        
                        # print("Arrive at BP (戻り終わりました。)")
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                        print(f"🤖 State:{state}")
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
                    else:
                        # print("NEXT BP:{}".format(BPLIST[-j]))
                        # print("NEXT BP:{}".format(next_position[0]))
                        # print("🔛 On the way BACK")                          # 一旦コメントアウト 0809

                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress

                    
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

                

            if TRIGAR:
                if BACK or bf:
                    try:
                        
                        if bf: # ストレスが溜まってから初回
                            # w = [round(0.1 * random.randint(1, 10), 2) for x in BPLIST]
                            # w = [0.8, 0.6, 0.2, 0.9, 0.4]
                            w = PROB # w = OBS # 🔑今は観測されている前提の簡単なやつ
                            w = OBS

                            print(f"🥌 WEIGHT = {w}")
                            # 手動で設定
                            print("手動で設定!!!!!")
                            print("PROB : {}".format(PROB))
                            

                            # BPLIST.append(state)
                            # bpindex = BPLIST.index(next_position[0])
                            Arc = [(abs(BPLIST[-1].row-BPLIST[x].row)) for x in range(len(BPLIST))]
                            print("👟 Arc[移動コスト]:{}".format(Arc))
                            index = Arc.index(0)
                            Arc.pop(index)
                            print("👟 Arc(remove 0[現在位置]):{}".format(Arc))
                            print("📂 Storage {}".format(BPLIST))
                            BPLIST.pop(-1)
                            print("📂 Storage(remove) {}".format(BPLIST))



                            
                        else:
                            print(f"🥌 WEIGHT = {w}")
                            print("👟 Arc[移動コスト]:{}".format(Arc))
                        bf = False
                        BACK = False
                        
                        # 2 つのリストの要素同士の演算
                        ##### WEIGHT CROSS で割っているので要らない
                        Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
                        # print(f"1/Arc = {Arc_INVERSE}")
                        ##### WEIGHT CROSS で割っているので要らない

                        # add 0808 正規化
                        w = np.round(preprocessing.minmax_scale(w), 3)
                        Arc = np.round(preprocessing.minmax_scale(Arc), 3)
                        Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
                        # print("📐正規化 w : {}, Arc : {}".format(w, Arc))
                        print("📐 正規化 WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))

                        # Arc = [0, 0]の時,Arc = [1, 1]に変更
                        if all(elem  == 0 for elem in Arc_INVERSE):
                            Arc_INVERSE = [1 for elem in Arc_INVERSE]
                            print("   Arc = [0, 0]の時, Arc_INVERSE : {}".format(Arc_INVERSE))
                        if all(elem  == 0 for elem in w):
                            w = [1 for elem in w]
                            print("   WEIGHT = [0, 0]の時, WEIGHT : {}".format(w))

                        # WEIGHT_CROSS = [round(x/y, 3) for x,y in zip(w,Arc)]
                        WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
                        print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))
                        # 歪んだサイコロを1000回振ってサンプルを得る
                        # next_position = random.choices(BPLIST, k = 1, weights = w)
                        # next_position = random.choices(BPLIST, k = 1, weights = Arc_INVERSE)
                        # next_position = random.choices(BPLIST, k = 1, weights = WEIGHT_CROSS)
                        # next_position = BPLIST[w.index(max(w))]
                        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]
                        # print("next_position : {}".format(next_position))
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{next_position}\n==================================")
                        on_the_way = True

                        
                    except:
                        print("ERROR!")
                        # STATE_HISTORY.append(state)
                        break
                
                if int(state.row) > int(next_position.row):
                    
                    TRIGAR2 = True
                    

                try:

                    if state == next_position:
                        
                        bpindex = BPLIST.index(next_position)
                        
                        # [Arc.append(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
                        Arc = [(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        index = Arc.index(0)
                        Arc.pop(index)
                        print("👟 Arc(remove 0[現在位置]):{}".format(Arc))


                        print("📂 Storage {}".format(BPLIST))
                        # BPLIST.remove(next_position[0])
                        BPLIST.remove(next_position)
                        
                        print("📂 Storage(remove) {}".format(BPLIST))

                        
                        # w.pop(bpindex)
                        w = np.delete(w, bpindex)  # 削除できていない
                        print("🥌 WEIGHT(remove):{}".format(w))
                        BACK =True


                        
                        # print("Arrive at BP (戻り終わりました。)!!!!!!!!!!!!")
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                        print(f"🤖 State:{state}")
                        STATE_HISTORY.append(state)
                        
                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress

                        



                        COUNT += 1
                        # add0807 これがないと通り過ぎてしまう(戻り過ぎる)
                        continue

                    else:
                        
                        if on_the_way:
                            on_the_way = False
                        else:
                            print("🔛 On the way BACK")
                            

                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress
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
               
                if not BRANCH:
                    
                    
                    if NODELIST[state.row][state.column] > 0.0:
                        ################################################
                        ################################################
                        # 本当はここで見つけた時に、現場情報のリストに格納していく

                        # model_edit_observation はここをコメントアウト↓
                        # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつ
                        print("Observation : {}".format(Observation))
                        OBS.append(Observation[state.row][state.column])
                        print("OBS : {}".format(OBS))
                        # 本当はここで見つけた時に、現場情報のリストに格納していく
                        # PROB.append(NODELIST[state.row][state.column]) # 今は仮にこれを使う
                        ################################################
                        ################################################
                        
                        print("🪧 NODE : ⭕️")
                        BPLIST.append(state)

                        STATE_HISTORY.append(state)

                        #####################################
                        STATE_HISTORY.append(state) # add0726
                        #####################################
                        
                        # 一個前が1ならpopで削除
                        print("📂 Storage {}".format(BPLIST))
                        length = len(BPLIST)

                    else: # elif NODELIST[state.row][state.column] == 0: 
                        print("🪧 NODE : ❌")

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

                        ##############################
                        # add 0808
                        BPLIST.append(state) # Arcを計算する為に、最初だけ必要
                        print("TEST STATE:{}, BPLIST:{}".format(state, BPLIST))
                        ##############################
                        
                        continue # add 0807
                
            print(f"🤖 State:{state}")
            STATE_HISTORY.append(state)
            print(f"Total Stress:{total_stress}")
            
            action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
            next_state, stress, done = env.step(action, TRIGAR, BRANCH)
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            
            COUNT += 1
            if COUNT > 30:
                break
         
        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
