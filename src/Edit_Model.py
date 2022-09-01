from enum import Enum
from tkinter import FIRST
from aem import con
import numpy as np
import random

from sklearn import preprocessing
from torch import t

from math import dist
from scipy.spatial import distance
import math

# ベースはEnv_model_prefer.py
# prefer(優先)は、stress -= 1 or stress = 0 することでその道を進みやすくしていた
# N = 1 が一つもないと BPlist = []だから、戻る場所がなくて、終了してしまう
# Env_bp/Env_model_prob_bp_2_Edit(match+cost).py の整理ver.
# model.py の整理ver.

# model_edit.py の分岐アリver.
# model_edit_2d.py の整理ver.
# model_edit_2d_Edit.py の編集ver.

# model_edit_2d_Edit_copy.py の整理ver.

# これが、分岐先もBPLISTに追加する最新ver. の整理ver. (0817)


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
            if BRANCH:
                print("BRANCH TRUE right 🌚 🌚 🌚")
                return (self.actions[3]) # add0817
            else:
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

    def get_distance(x1, y1, x2, y2):
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d
        


def main():

    
    
    
    NODELIST = [
            [0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]

    NODE_COUNT = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0] # start
    ]

    TURNING_POINT = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0] # start
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
            [0,   0,   0,   0.8, 0.7, 0],
            [0.4, 0.9, 0.4, 0.5, 0, 0],
            [0.9, 0.5, 0.7, 0.3, 0, 0], # 0.8
            [0.2, 0.8, 0.5, 0, 0, 0],
            [0.6, 0.4, 0.6, 0, 0, 0],
            [0.8, 0.7, 0.3, 0, 0, 0],
            [1,   0,   0,   0, 0, 0] # start
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
        save = 0
        save_trigar = False
        
        FIRST = True
        Stressfull = 1 #3
        BACK = False
        BACK2 = False

        BACK3 = False
        bf = True
        
        TRIGAR2 = False
        ########## parameter ##########

        PROB = []
        Arc = []
        OBS = []

        BPLIST_2 = []

        on_the_way = False

        ADD = False
        ADD2 = False

        test = False
        
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
                    
                    print("next position     BACK2:{}".format(BACK2))
                    print(Arc_INVERSE,Arc)
                    try:
                        print(f"🥌 WEIGHT = {w}")
                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        
                        # 2 つのリストの要素同士の演算
                        ##### WEIGHT CROSS で割っているので要らない
                        try:
                        
                            Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
                        except:
                        
                            Arc_INVERSE = [0]
                        # print(f"1/Arc = {Arc_INVERSE}")
                        ##### WEIGHT CROSS で割っているので要らない

                        # add 0808 正規化
                        w = np.round(preprocessing.minmax_scale(w), 3)
                        Arc = np.round(preprocessing.minmax_scale(Arc), 3)

                        try:
                            Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
                        
                        except:
                            
                            print("Ain:{}".format(Arc_INVERSE))
                            pass
                        
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

                        # add0818
                        if all(elem  == 0 for elem in WEIGHT_CROSS):
                            print("WEIGHT CROSSは全部0です。")
                            
                            Arc = Arc.tolist()
                            print("Arc type : {}".format(type(Arc)))
                            near_index = Arc.index(min(Arc))
                            print("Arc:{}, index:{}".format(Arc, near_index))
                            WEIGHT_CROSS[near_index] = 1
                            print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))
                        # 歪んだサイコロを1000回振ってサンプルを得る
                        # next_position = random.choices(BPLIST, k = 1, weights = w)
                        # next_position = random.choices(BPLIST, k = 1, weights = Arc_INVERSE)
                        # next_position = random.choices(BPLIST, k = 1, weights = WEIGHT_CROSS)
                        # next_position = BPLIST[w.index(max(w))]
                        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]
                        
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{next_position}\n==================================")
                        on_the_way = True
                        print(f"🤖 State:{state}")
                        
                        # どっちでもいい 0817 (おそらく二個以上戻るときに必要)
                        # BACK2 = False
                        # 今後の為に一応追加 (おそらく二個以上戻るときに必要)
                        # BACK = False
                    # except:
                    except Exception as e:
                        # print('=== エラー内容 ===')
                        # print('type:' + str(type(e)))
                        # print('args:' + str(e.args))
                        # print('message:' + e.message)
                        # print('e自身:' + str(e))
                        print("ERROR! test")
                        # STATE_HISTORY.append(state)
                        break


                    # continue
                    
                # if int(state.row) < int(next_position[0].row):
                if not BRANCH:
                    if int(state.row) < int(next_position.row):
                        print("これが出ていればここが問題 trigar2")
                        
                        TRIGAR2 = False
                        
                        COUNT += 1
                elif BRANCH:
                    if int(state.column) > int(next_position.column):
                        print("🌚 🌚 🌚")
                        
                        TRIGAR2 = False
                        
                        COUNT += 1
                    
                try:
                    
                    
                    # 🔑戻った後の行動決定

                    # if state == next_position[0]:
                    if state == next_position:
                        # add0819
                        NODE_COUNT[state.row][state.column] += 1
                        print("NODE_COUNT = {} TRIGAR2🍎".format(NODE_COUNT))

                        # bpindex = BPLIST.index(next_position[0])
                        bpindex = BPLIST.index(next_position) # 現在地
                        
                        Arc = [math.sqrt((BPLIST[bpindex].row - BPLIST[x].row) ** 2 + (BPLIST[bpindex].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]

                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        index = Arc.index(0)
                        Arc.pop(index)
                        print("👟 Arc(remove 0[現在位置]):{}".format(Arc))
                        print("📂 Storage {}".format(BPLIST))
                        # BPLIST.remove(next_position[0])
                        BPLIST.remove(next_position)
                        print("📂 Storage(remove) {}".format(BPLIST))

                        print("📂 OBS 削除前 : {}".format(OBS))
                        OBS.pop(bpindex)
                        print("📂 OBS(remove) : {}".format(OBS))

                        
                        BACK2 = True

                        
                        # w.pop(bpindex)
                        w = np.delete(w, bpindex)  # 削除できていない Arcは毎回入れ直しているからpopが使える
                        print("🥌 WEIGHT(remove):{}".format(w))
                        # Arc.pop(bpindex)

                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。test🌝)")
                        print(f"🤖 State:{state}")
                        STATE_HISTORY.append(state)
                        
                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress



                        COUNT += 1

                        if not BRANCH:
                            print("分岐 TRUE!!!!!!!!!!!!!!")
                            BRANCH = True
                            TRIGAR = False
                            
                        else:
                            
                            print("分岐 FALSE!!!!!!!!!!!!! -> True のまま")
                            

                            ########################
                            if state.column != 0:
                                BRANCH = False
                                TRIGAR = False
                            ########################
                            
                            ####################
                            print("🪐 🪐 🪐 🪐 🪐BACK = {}".format(BACK)) # 一回しかここには入らない
                            "なぜか -> BRANCHの時に戻り終わった時に、周辺探索(上)を見ない為、分岐終了とならずに、BACK = True にならないから"
                            "というか、TRIGAR の BACKには本線で初めて TRIGAR になった時のみ入る"
                            
                            
                            BACK = True # add0818
                            ####################
                            

                        if int(state.row) > int(next_position.row):
                            
                            TRIGAR2 = True # コメントアウト0817
                        else: # int(state.row) <= int(next_position.row):
                            
                            TRIGAR2 = False

                        
                        # add0817
                        if int(state.column) < int(next_position.column):
                            pass

                        else: # int(state.row) <= int(next_position.row):
                            
                            TRIGAR2 = False
                        print("BRANCH : {}".format(BRANCH))


                        # add0807
                        # continue  # 0816 ここら辺のエラーでwが重複している
                        # TRIGAR の時はcontinueを消せば良かったが、TRIGAR2の時は、TRIGAR = FALSEに入って○になってしまう
                        
                        
                        print(f"🤖 State:{state}")
                        STATE_HISTORY.append(state)
                        print(f"Total Stress:{total_stress}")
                        

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
                    print("これ以上戻れません。 終了します。!!!!!")
                    # ストレスをマイナスにさせない為に追加
                    # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                    # probablity
                    if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        if total_stress + stress >= 0:
                            total_stress += stress
                    break

                

            if TRIGAR:
                # print("next position:{}".format(next_position))
                print("next position     BACK:{}".format(BACK))
                if BACK or bf:
                    print("next position!!!!!!")
                    try:
                        
                        if bf: # ストレスが溜まってから初回
                            
                            # 🔑今は観測されている前提の簡単なやつ
                            w = OBS

                            print(f"🥌 WEIGHT = {w}")
                            # 手動で設定
                            print("手動で設定!!!!! 0816")
                            
                            

                            bpindex = BPLIST.index(state)
                            print("index:{}".format(bpindex))
                            if not BRANCH:
                                
                                Arc = [math.sqrt((BPLIST[bpindex].row - BPLIST[x].row) ** 2 + (BPLIST[bpindex].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]
                            else:

                                Arc = [math.sqrt((BPLIST[bpindex].row - BPLIST[x].row) ** 2 + (BPLIST[bpindex].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]

                                
                                
                            print("🥌 WEIGHT(remove):{}".format(w))
                            print("👟 Arc[移動コスト] 0816 :{}".format(Arc))
                            index = Arc.index(0)
                            Arc.pop(index)
                            print("👟 Arc(remove 0[現在位置]):{}".format(Arc))
                            print("📂 Storage {}".format(BPLIST))
                            
                            BPLIST.pop(bpindex)
                            print("📂 Storage(remove) {}".format(BPLIST))
                        else:
                            print(f"🥌 WEIGHT = {w}")
                            print("👟 Arc[移動コスト]:{}".format(Arc))
                        
                        try:
                            
                            Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
                        except:
                        
                            Arc_INVERSE = [0]
                        print(f"1/Arc = {Arc_INVERSE}")
                        ##### WEIGHT CROSS で割っているので要らない

                        # add 0808 正規化
                        w = np.round(preprocessing.minmax_scale(w), 3)
                        Arc = np.round(preprocessing.minmax_scale(Arc), 3)
                        
                        if Arc_INVERSE != 0:
                            Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
                        else:
                            
                            pass
                        
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

                        # add0818
                        if all(elem  == 0 for elem in WEIGHT_CROSS):
                            print("\nWEIGHT CROSSは全部0です。1")
                            Arc = Arc.tolist()
                            print("Arc type : {}".format(type(Arc)))
                            near_index = Arc.index(min(Arc))
                            print("Arc:{}, index:{}".format(Arc, near_index))
                            WEIGHT_CROSS[near_index] = 1
                            print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))
                        # 歪んだサイコロを1000回振ってサンプルを得る
                        # next_position = random.choices(BPLIST, k = 1, weights = w)
                        # next_position = random.choices(BPLIST, k = 1, weights = Arc_INVERSE)
                        # next_position = random.choices(BPLIST, k = 1, weights = WEIGHT_CROSS)
                        # next_position = BPLIST[w.index(max(w))]
                        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{next_position}\n==================================")
                        on_the_way = True
                        print(f"🤖 State:{state}")

                        bf = False
                        BACK = False
                        BACK2 = False
                    except Exception as e:
                        # print('=== エラー内容 ===')
                        # print('type:' + str(type(e)))
                        # print('args:' + str(e.args))
                        # print('message:' + e.message)
                        # print('e自身:' + str(e))
                        print("ERROR!")
                        
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。test)")
                        print(f"🤖 State:{state}")
                        STATE_HISTORY.append(state) # 0815
                        
                        break

                    
                        
                try:
                    
                    # 🔑戻った後の行動決定
                    
                    # if state == next_position[0]:
                    if state == next_position:
                        
                        NODE_COUNT[state.row][state.column] += 1
                        print("NODE_COUNT = {} TRIAGR🍏".format(NODE_COUNT))

                        
                        bpindex = BPLIST.index(next_position) 
                        "次に戻る場所がない(BPLIST = [])とここでエラーが出るので、L576で BACK = True にすることで、next position を設定し直す"
                        
                        
                        if not BRANCH:
                            
                            Arc = [math.sqrt((BPLIST[bpindex].row - BPLIST[x].row) ** 2 + (BPLIST[bpindex].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]

                        else:
                            
                            Arc = [math.sqrt((BPLIST[bpindex].row - BPLIST[x].row) ** 2 + (BPLIST[bpindex].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]
                        
                        print("👟 Arc[移動コスト]:{}".format(Arc))
                        index = Arc.index(0)
                        
                        Arc.pop(index)
                        print("👟 Arc(remove 0[現在位置]):{}".format(Arc))
                        print("📂 Storage {}".format(BPLIST))
                        
                        BPLIST.remove(next_position)
                        print("📂 Storage(remove) {}".format(BPLIST))
                        print("📂 OBS 0816 削除前 {}".format(OBS))
                        OBS.pop(bpindex)
                        print("📂 OBS(remove)     {}".format(OBS))

                        w = OBS
                        print("🥌 WEIGHT(remove):{}".format(w))
                        BACK = True

                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)🐬")
                        # BACK3 = True
                        print(f"🤖 State:{state}")
                        STATE_HISTORY.append(state)
                        
                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress

                        



                        COUNT += 1

                        if not BRANCH:
                            print("分岐 TRUE 0816")
                            BRANCH = True
                            TRIGAR = False
                        else:
                            
                            print("分岐 FALSE")
                            
                            ########################
                            if state.column != 0:
                                BRANCH = False
                                TRIGAR = False
                            ########################
                            

                        print("TRIGAR={}, TRIGAR2={}, BRANCH={}".format(TRIGAR, TRIGAR2, BRANCH))
                        # add0807 これがないと通り過ぎてしまう(戻り過ぎる)
                        continue
                    else:
                        
                        # 分岐から本線に戻ってきた時に、BRANCH = Falseにする + nextが上ならTRIGAR2 = Trueにする
                        # if state.column == 0:
                        print("🌕 next position column : {}, BRANCH : {} 🌟".format(next_position.column, BRANCH))


                        if state.column == next_position.column: # 🌝重要 0818 今は本線がcolumn = 0 の時だから、0の時のみ上に上がれる
                            print("🌕")
                            BRANCH = False # Falseにすると、いずれ同じ行の分岐の位置にあるときに破綻する(column = column ... [2, 3] と [1, 3] のような関係)

                            if int(state.row) > int(next_position.row):
                                
                                TRIGAR2 = True
                            else:
                                TRIGAR2 = False

                        ####################### add 0818 #######################
                        elif state.column == 0:
                            BRANCH = False
                            if int(state.row) > int(next_position.row):
                                
                                TRIGAR2 = True
                            else:
                                
                                TRIGAR2 = False
                        ####################### add 0818 #######################

                        print("TRIGAR:{} TRIGAR2:{} BRANCH:{}".format(TRIGAR, TRIGAR2, BRANCH))

                        # 分岐している時に、nextが右ならTRIGAR3 = Trueにする
                        if state.row == next_position.row:
                            print("next position row : {}".format(next_position.row))
                            BRANCH = True # ここでBRANCH = True にしているので、上でBRANCH = False になっても、next position が分岐先の時は(state row == next position row)分岐できる
                            
                            
                            if int(state.column) < int(next_position.column):
                                
                                print("TRIGAR:{} TRIGAR2:{} BRANCH:{}".format(TRIGAR, TRIGAR2, BRANCH))
                                
                                
                                TRIGAR2 = True
                            else:
                                
                                TRIGAR2 = False

                                
                                # 今だけの解決策
                                # if TURNING_POINT[next_position.row][next_position.column] == 1:
                                print(state.row, state.column, next_position.row, next_position.column)
                                # add0820
                                # if TURNING_POINT[state.row][0] != 1: # True
                                #     print("TEST 0820 🍊")
                                #     BRANCH = False
                                #     test = True
                                # add0820

                        # add0820
                        # if TURNING_POINT[state.row][0] == 1: #  and test:
                        #     print("TEST 0820 🍊🍊")
                        #     BRANCH = True
                        #     if state.row == next_position.row:
                        #         BRANCH = False

                            


                        if on_the_way:
                            on_the_way = False
                        else:
                            print("🔛 On the way BACK 🌟")
                            

                        # ストレスをマイナスにさせない為に追加
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # 1つ前の状態で０の場合1減らす 進む時、次が0の時にストレスが増えているから
                        # probablity
                        if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                            if total_stress + stress >= 0:
                                total_stress += stress
                
                except Exception as e:
                    # print('=== エラー内容 ===')
                    # print('type:' + str(type(e)))
                    # print('args:' + str(e.args))
                    # print('message:' + e.message)
                    # print('e自身:' + str(e))

                    print("state:{}".format(state))
                    print("これ以上戻れません。 終了します。!")
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
                    
                    # if NODELIST[state.row][state.column] == 1:
                    if NODELIST[state.row][state.column] > 0.0:
                        print("🪧 NODE : ⭕️")
                        # if NODE_COUNT[state.row][state.column] < 1: # < 2: # 1回目の時は　BPLIST に追加
                        #     print("初めて観測")
                        #     ################################################
                        #     ################################################
                        #     # 本当はここで見つけた時に、現場情報のリストに格納していく
                        #     # model_edit_observation はここをコメントアウト↓
                        #     # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつ
                        #     print("Observation : {}".format(Observation))
                        #     OBS.append(Observation[state.row][state.column])
                        #     print("OBS : {}".format(OBS))
                        #     # 本当はここで見つけた時に、現場情報のリストに格納していく
                        #     ################################################
                        #     ################################################
                        #     BPLIST.append(state)
                        # elif TURNING_POINT[state.row][state.column] == 1:
                        #     print("TURNING POINT 🚦 🚦 🚦")
                        #     BPLIST.append(state)
                        if NODE_COUNT[state.row][state.column] < 1 or TURNING_POINT[state.row][state.column] == 1: # < 2: # 1回目の時は　BPLIST に追加
                            print("初めて観測")
                            if TURNING_POINT[state.row][state.column] == 1: # add0820
                                print("TURNING POINT 🚦 🚦 🚦")
                            
                            # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつprint("Observation : {}".format(Observation))
                            # OBS.append(Observation[state.row][state.column])
                            
                            print("📂 Storage BRANCH {}".format(BPLIST))

                            try:
                                length = len(BPLIST)
                                print("len={}".format(length))
                                print("📂 Storage BRANCH {}".format(BPLIST))
                                for test in range (length):
                                    
                                    # if BPLIST[(length-1)-test].row == state.row:
                                    if BPLIST[(length-1)-test].row >= state.row:
                                        
                                        BPLIST.insert((length-1)-test+1,state)
                                        OBS.insert((length-1)-test+1,Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                        
                                        save = (length -1) - test + 1
                                        save_trigar = True
                                        ADD = True

                                        break

                                if length == 1:
                                    BPLIST.insert((length-1)+1,state)
                                    OBS.insert((length-1)+1,Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                    ADD = True
                                elif length == 0:
                                    BPLIST.append(state)
                                    OBS.append(Observation[state.row][state.column])
                                    ADD = True
                                
                                print("📂 Storage BRANCH {}".format(BPLIST))
                                if not ADD:
                                    print("🌝0817 TEST")
                                    BPLIST.insert(0, state)
                                    OBS.insert(0, Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                    
                                    # save = (length -1) - test + 1
                                    # save_trigar = True
                                    # break
                                
                                ADD = False
                                print("📂 Storage BRANCH {}".format(BPLIST))
                            except:
                                pass


                        STATE_HISTORY.append(state)

                        #####################################
                        STATE_HISTORY.append(state) # add0726
                        #####################################
                        
                        # 一個前が1ならpopで削除 -> 連続しているノードを削除する場合
                        print("📂 Storage {}".format(BPLIST))
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
                        print("🪧 NODE : ❌")

                    print("Δs = {}".format(stress))
                    ##############################
                    if total_stress + stress >= 0:
                    ##############################
                        total_stress += stress

                    if total_stress >= Stressfull:
                        TRIGAR = True
                        print("=================")
                        print("FULL ! MAX! 🔙⛔️⭐️")
                        print("=================")
                        ##################################
                        STATE_HISTORY.append(state) # 0729
                        ##################################
                        COUNT += 1

                        ##############################
                        BPLIST.append(state) # Arcを計算する為に、最初だけ必要
                        print("TEST STATE:{}, BPLIST:{}".format(state, BPLIST))
                        ##############################

                        print(BACK, BACK2, bf, prev_state)
                        # BACK =True
                        # BACK2 =True
                        bf = True
                        
                        continue
                else: # 分岐は使わないので一旦コメントアウト0807
                    ##############################
                    if total_stress + stress >= 0:
                    ##############################
                        total_stress += stress
                    print("Δs = {}".format(stress))

                    if total_stress >= Stressfull:
                        print("=================")
                        print("FULL ! MAX! 🔙⛔️")
                        print("=================")
                        print("分岐終了!")
                        print("TRIGAR2:{}".format(TRIGAR2))
                        STATE_HISTORY.append(state)
                        TRIGAR = True
                        # BACK =True # add0815
                        # BACK2 = True # add0815
                        ##############################
                        # BPLIST.append(state) # Arcを計算する為に、最初だけ必要
                        length = len(BPLIST)
                        print("len={}".format(length))
                        # 何をしている？0817
                        for test in range (length):
                            if BPLIST[(length-1)-test].row >= state.row:
                                BPLIST.insert((length-1)-test+1,state)
                                ADD2 = True
                                break
                        
                        if length == 1:
                            BPLIST.insert((length-1)+1,state)
                            ADD2 = True
                        elif length == 0:
                            ADD2 = True
                            BPLIST.append(state)
                        ##############################

                        if not ADD2:
                            print("🌝🍏0819 TEST")
                            BPLIST.insert(0, state)
                            OBS.insert(0, Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時

                        ADD2 = False
                        print(f"🤖 State:{state}")
                        COUNT += 1
                        bf = True
                        print("OBS 分岐!!!!!: {}".format(OBS))
                        print("📂 Storage BRANCH {}".format(BPLIST))
                        if length == 0:
                            pass
                        else:
                            continue # コメントアウト 0817 ここでcontinueすることで、分岐終了時にその場に止まって次の位置を決める為に必要
                    else:
                        TRIGAR = False

                        # if NODELIST[state.row][state.column] == 1:
                        if NODELIST[state.row][state.column] > 0.0:
                            
                            print("🪧 NODE : ⭕️")                                # add0820
                            if NODE_COUNT[state.row][state.column] < 1 or TURNING_POINT[state.row][state.column] == 1: # < 2: # 1回目の時は　BPLIST に追加
                                print("初めて観測")

                                if TURNING_POINT[state.row][state.column] == 1: # add0820
                                    print("TURNING POINT 🚦 🚦 🚦")
                                
                                print("Observation : {}".format(Observation))
                                # OBS.append(Observation[state.row][state.column])
                                
                                print("📂 Storage BRANCH {}".format(BPLIST))

                                try:
                                    length = len(BPLIST)
                                    print("len={}".format(length))
                                    print("📂 Storage BRANCH {}".format(BPLIST))
                                    for test in range (length):
                                        
                                        # if BPLIST[(length-1)-test].row == state.row:
                                        if BPLIST[(length-1)-test].row >= state.row:
                                            
                                            BPLIST.insert((length-1)-test+1,state)
                                            OBS.insert((length-1)-test+1,Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                            
                                            save = (length -1) - test + 1
                                            save_trigar = True
                                            ADD = True

                                            break

                                    if length == 1:
                                        BPLIST.insert((length-1)+1,state)
                                        OBS.insert((length-1)+1,Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                        ADD = True
                                    elif length == 0:
                                        BPLIST.append(state)
                                        OBS.append(Observation[state.row][state.column])
                                        ADD = True
                                    
                                    print("📂 Storage BRANCH {}".format(BPLIST))
                                    if not ADD:
                                        print("🌝0817 TEST")
                                        BPLIST.insert(0, state)
                                        OBS.insert(0, Observation[state.row][state.column])  # -2 は w or obs で[2, 0] を削除してない時
                                        
                                        # save = (length -1) - test + 1
                                        # save_trigar = True
                                        # break
                                    
                                    ADD = False

                                    print("📂 Storage BRANCH {}".format(BPLIST))
                                except:
                                    
                                    pass

                            print(f"📂Storage:{BPLIST}")
                            STATE_HISTORY.append(state) # add0819
                            STATE_HISTORY.append(state)
                            
                            ############################
                            # 分岐先は削除しなくてもいいかも#
                            ############################
                            # 一個前が1ならpopで削除
                            length = len(BPLIST)

                            # コメントアウト 0806
                            # if length > 1:
                            #     if not state.column-1 == 0:
                            #         # if NODELIST[state.row][state.column-1] == 1:
                            #         if NODELIST[state.row][state.column] > 0.0:
                            #             print("Branch方向 削除前 {}".format(BPLIST))
                            #             if save_trigar:
                            #                 BPLIST.pop(-(length + 1 - save))
                            #                 save_trigar = False
                            #             else:
                            #                 BPLIST.pop(-2)
                            #             print("Branch方向 削除後 {}".format(BPLIST))
                            # コメントアウト 0806
                            
                        else: # elif NODELIST[state.row][state.column] == 0: 
                            print("🪧NODE : ❌")
            
            
            print(f"🤖 State:{state}")
            STATE_HISTORY.append(state)
            print(f"Total Stress:{total_stress}")
            

            action = agent.policy(state, TRIGAR, BRANCH, TRIGAR2)
            next_state, stress, done = env.step(action, TRIGAR, BRANCH)
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            
            COUNT += 1
            if COUNT > 100:
                break
            
        
        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
