import math
from tkinter import RIGHT

from numpy import average
import random
import collections

# self.actions[0] -> i =  1 (โ)UP
# self.actions[1] -> i = -1 (โ)DOWN
# self.actions[2] -> i =  2 (โ)LEFT
# self.actions[3] -> i = -2 (โ)RIGHT

class Agent():

    def __init__(self):
        
        self.V_0_LIST = []
        self.V_1_LIST = []
        self.V_2_LIST = []
        self.V_3_LIST = []

        self.Episode_0 =[[], [], []]
        self.Episode_1 =[[], [], []]
        self.Episode_2 =[[], [], []]
        self.Episode_3 =[[], [], []]

        self.UP = 1
        self.DOWN = -1
        self.LEFT = 2
        self.RIGHT = -2
        self.A_0 = [self.LEFT, self.RIGHT] # At
        # A_1 = [DOWN, LEFT, RIGHT] # At
        self.A_1 = [self.LEFT, self.RIGHT] # At
        # A_2 = [UP, DOWN, LEFT] # At
        self.A_2 = [self.UP, self.DOWN] # At
        # A_3 = [UP, DOWN, RIGHT] # At
        self.A_3 = [self.UP, self.DOWN] # At

        self.V_0 = [0]*2
        self.V_1 = [0]*2
        self.V_2 = [0]*2
        self.V_3 = [0]*2
        length_0 = len(self.Episode_0[0])
        length_1 = len(self.Episode_1[0])
        length_2 = len(self.Episode_2[0])
        length_3 = len(self.Episode_3[0])
        
        self.L_0 = [length_0]*2
        self.L_1 = [length_1]*2
        self.L_2 = [length_2]*2
        self.L_3 = [length_3]*2

    def policy(self, prev_action, ave_0, ave_1, ave_2, ave_3): # , A_0, A_1, A_2, A_3):

        print("\n----- ๐ค๐ agent policy -----")
        
        

        if prev_action == 1:
            print("๐ At โ ")
            try:
                print("\n----- โ ๏ธใๅ่กๅใใจใฎๅนณๅไพกๅคใไธ็ชๅคงใใ่กๅใ้ธๆ-----")
                maxIndex_0 = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
                print("\nMAX INDEX_0 : {}".format(maxIndex_0))
                if len(maxIndex_0) > 1:
                    print("ๅนณๅไพกๅคใฎๆๅคงใ่คๆฐๅใใใพใใ")
                    maxIndex_0 = [random.choice(maxIndex_0)]
                    print("ใฉใณใใ ใง ave_0{} = {} ใ้ธๆใใพใใใ".format(maxIndex_0, self.A_0[maxIndex_0[0]]))
                else:
                    print("ๅนณๅไพกๅคใฎๆๅคงใไธใคใใใพใใ")
                # next_action_0 = A_0[maxIndex_0[0]]
                next_action = self.A_0[maxIndex_0[0]]
                print("At-1 = โฌ๏ธ  ใฎๆใๆฌกใฎ่กๅAt : {}, t-1ใพใงใฎๅนณๅไพกๅค : {}".format(next_action, max(ave_0)))
            # except:
            except Exception as e:
                print(ave_0)
                print('=== ใจใฉใผๅๅฎน ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e่ช่บซ:' + str(e))
                print("ERROR")
                # next_action_0 = random.choice(A_0)
                next_action = random.choice(self.A_0)
                print("ใฉใณใใ ใง {} ใ้ธๆใใพใใใ".format(next_action))

        if prev_action == -1:
            print("๐ At โก")
            try:
                maxIndex_1 = [i for i, x in enumerate(ave_1) if x == max(ave_1)]
                print("\nMAX INDEX_1 : {}".format(maxIndex_1))
                if len(maxIndex_1) > 1:
                    print("ๅนณๅไพกๅคใฎๆๅคงใ่คๆฐๅใใใพใใ")
                    maxIndex_1 = [random.choice(maxIndex_1)]
                    print("ใฉใณใใ ใง ave_1{} = {} ใ้ธๆใใพใใใ".format(maxIndex_1, self.A_1[maxIndex_1[0]]))
                else:
                    print("ๅนณๅไพกๅคใฎๆๅคงใไธใคใใใพใใ")
                # next_action_1 = A_1[maxIndex_1[0]]
                next_action = self.A_1[maxIndex_1[0]]
                print("At-1 = โฌ๏ธ  ใฎๆใๆฌกใฎ่กๅAt : {}, t-1ใพใงใฎๅนณๅไพกๅค : {}".format(next_action, max(ave_1)))
            # except:
            except Exception as e:
                print(ave_1)
                print('=== ใจใฉใผๅๅฎน ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e่ช่บซ:' + str(e))
                print("ERROR")
                # next_action_1 = random.choice(A_1)
                next_action = random.choice(self.A_1)
                print("ใฉใณใใ ใง {} ใ้ธๆใใพใใใ".format(next_action))

        if prev_action == 2:
            print("๐ At โข")
            try:
                maxIndex_2 = [i for i, x in enumerate(ave_2) if x == max(ave_2)]
                print("\nMAX INDEX_2 : {}".format(maxIndex_2))
                if len(maxIndex_2) > 1:
                    print("ๅนณๅไพกๅคใฎๆๅคงใ่คๆฐๅใใใพใใ")
                    maxIndex_2 = [random.choice(maxIndex_2)]
                    print("ใฉใณใใ ใง ave_2{} = {} ใ้ธๆใใพใใใ".format(maxIndex_2, self.A_2[maxIndex_2[0]]))
                else:
                    print("ๅนณๅไพกๅคใฎๆๅคงใไธใคใใใพใใ")
                # next_action_2 = A_2[maxIndex_2[0]] # 1 or -1
                next_action = self.A_2[maxIndex_2[0]] # 1 or -1
                print("At-1 = โฌ๏ธ  ใฎๆใๆฌกใฎ่กๅAt : {}, t-1ใพใงใฎๅนณๅไพกๅค : {}".format(next_action, max(ave_2)))
            # except:
            except Exception as e:
                print('=== ใจใฉใผๅๅฎน ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e่ช่บซ:' + str(e))
                print("ERROR")
                # next_action_2 = random.choice(A_2)
                next_action = random.choice(self.A_2)
                print("ใฉใณใใ ใง {} ใ้ธๆใใพใใใ".format(next_action))

        if prev_action == -2:
            print("๐ At โฃ")
            try:
                maxIndex_3 = [i for i, x in enumerate(ave_3) if x == max(ave_3)]
                print("\nMAX INDEX_3 : {}".format(maxIndex_3))
                if len(maxIndex_3) > 1:
                    print("ๅนณๅไพกๅคใฎๆๅคงใ่คๆฐๅใใใพใใ")
                    maxIndex_3 = [random.choice(maxIndex_3)]
                    print("ใฉใณใใ ใง ave_3{} = {} ใ้ธๆใใพใใใ".format(maxIndex_3, self.A_3[maxIndex_3[0]]))
                else:
                    print("ๅนณๅไพกๅคใฎๆๅคงใไธใคใใใพใใ")
                # next_action_3 = A_3[maxIndex_3[0]] # 1 or -1
                next_action = self.A_3[maxIndex_3[0]] # 1 or -1
                print("At-1 = โฌ๏ธ  ใฎๆใๆฌกใฎ่กๅAt : {}, t-1ใพใงใฎๅนณๅไพกๅค : {}".format(next_action, max(ave_3)))
            # except:
            except Exception as e:
                print('=== ใจใฉใผๅๅฎน ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e่ช่บซ:' + str(e))
                print("ERROR")
                # next_action_3 = random.choice(A_3)
                next_action = random.choice(self.A_3)
                print("ใฉใณใใ ใง {} ใ้ธๆใใพใใใ".format(next_action))
        

        

        
        
        return next_action

    def value(self):

        print("\n----- โ ๏ธ  ้กไผผใจใใฝใผใ(At-1)ใใจใซไพกๅค่จ็ฎ-----\n")

        


        print("๐ len = {}".format(len(self.Episode_2[0])))
        # print(self.Episode_1)
        for i in range(len(self.Episode_0[0])):
            
            if self.Episode_0[1][i] ==  2:
                # V_0[2] += self.E_0[2][i]
                self.V_0[0] += self.Episode_0[2][i]
            if self.Episode_0[1][i] == -2:
                # V_0[3] += self.E_0[2][i]
                self.V_0[1] += self.Episode_0[2][i]

        
        for i in range(len(self.Episode_1[0])):
            
                if self.Episode_1[1][i] ==  2:
                    # V_1[2] += self.E_1[2][i]
                    self.V_1[0] += self.Episode_1[2][i]
                if self.Episode_1[1][i] == -2:
                    # V_1[3] += self.E_1[2][i]
                    self.V_1[1] += self.Episode_1[2][i]
        
        
        for i in range(len(self.Episode_2[0])):
                print("๐ ๐ ๐ 2")
                if self.Episode_2[1][i] ==  1:
                    print("๐ ๐ ๐ 22")
                    self.V_2[0] += self.Episode_2[2][i]
                if self.Episode_2[1][i] == -1:
                    self.V_2[1] += self.Episode_2[2][i]
                # if self.E_2[1][i] ==  2:
                #     V_2[2] += self.E_2[2][i]
                # if self.E_2[1][i] == -2:
                #     V_2[3] += self.E_2[2][i]

        for i in range(len(self.Episode_3[0])):
            print("๐ ๐ ๐3")
            if self.Episode_3[1][i] ==  1:
                self.V_3[0] += self.Episode_3[2][i]
            if self.Episode_3[1][i] == -1:
                self.V_3[1] += self.Episode_3[2][i]
            # if self.E_3[1][i] ==  2:
            #     V_3[2] += self.E_3[2][i]
            # if self.E_3[1][i] == -2:
            #     V_3[3] += self.E_3[2][i]

        print("----- โ ๏ธใV = ๅ่กๅๅพใซๅพใๅ ฑ้ฌใฎ็ทๅ-----")
        print(" V_0[LEFT, RIGHT] :{}, L : {}".format(self.V_0, self.L_0))
        print(" V_1[LEFT, RIGHT] :{}, L : {}".format(self.V_1, self.L_1))
        print(" V_2[UP,   DOWN]  :{}, L : {}".format(self.V_2, self.L_2))
        print(" V_3[UP,   DOWN]  :{}, L : {}\n".format(self.V_3, self.L_3))

        try:
            ave_0 = [self.V_0[x] / self.L_0[x] for x in range(len(self.V_0))]
        except:
            ave_0 = self.V_0 # [0] # 0
        print("ไพกๅค V_0 [LEFT, RIGHT] = {}".format(self.V_0))
        print("ไพกๅคใฎๅนณๅ[LEFT, RIGHT] : {}".format(ave_0))
        try:
            ave_1 = [self.V_1[x] / self.L_1[x] for x in range(len(self.V_1))]
        except:
            ave_1 = self.V_1 # [0] # 0
        print("ไพกๅค V_1 [LEFT, RIGHT] = {}".format(self.V_1))
        print("ไพกๅคใฎๅนณๅ[LEFT, RIGHT] : {}".format(ave_1))
        try:
            ave_2 = [self.V_2[x] / self.L_2[x] for x in range(len(self.V_2))]
        except:
            ave_2 = self.V_2 # [0] # 0
        print("ไพกๅค V_2 [UP, DOWN] = {}".format(self.V_2))
        print("ไพกๅคใฎๅนณๅ[UP, DOWN] : {}".format(ave_2))
        try:
            ave_3 = [self.V_3[x] / self.L_3[x] for x in range(len(self.V_3))]
        except:
            ave_3 = self.V_3 # [0] # 0
        print("ไพกๅค V_3 [UP, DOWN] = {}".format(self.V_3))
        print("ไพกๅคใฎๅนณๅ[UP, DOWN] : {}".format(ave_3))

        

        return ave_0, ave_1, ave_2, ave_3


    def save_episode(self, prev_action, action):

        if prev_action == self.LEFT: # LEFT
            self.Episode_2[0].append(prev_action)
            self.Episode_2[1].append(action)                           # At-1 = LEFTใฎๆใฎ At(โ โ)
            
            if action == self.UP:
                print("โก๏ธ LEFT -> UP Rt = 1")
                self.Episode_2[2].append(1) # ไปใฏๆฌกใฎ่กๅใงๅฟใ็บ่ฆใงใใๅๆ(R = 1)
                print("Episode2 : {}".format(self.Episode_2))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_2[2].append(0)

        if prev_action == self.RIGHT: # LEFT
            self.Episode_3[0].append(prev_action)
            self.Episode_3[1].append(action)                           # At-1 = LEFTใฎๆใฎ At(โ โ)
            
            if action == self.UP:
                print("โก๏ธ RIGHT -> UP Rt = 1")
                self.Episode_3[2].append(1) # ไปใฏๆฌกใฎ่กๅใงๅฟใ็บ่ฆใงใใๅๆ(R = 1)
                print("Episode3 : {}".format(self.Episode_3))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_3[2].append(0)

        if prev_action == self.UP: # LEFT
            self.Episode_0[0].append(prev_action)
            self.Episode_0[1].append(action)                           # At-1 = LEFTใฎๆใฎ At(โ โ)
            
            if action == self.UP:
                print("โก๏ธ UP -> UP Rt = 1")
                self.Episode_0[2].append(1) # ไปใฏๆฌกใฎ่กๅใงๅฟใ็บ่ฆใงใใๅๆ(R = 1)
                print("Episode0 : {}".format(self.Episode_0))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_0[2].append(0)
        
        if prev_action == self.DOWN: # LEFT
            self.Episode_1[0].append(prev_action)
            self.Episode_1[1].append(action)                           # At-1 = LEFTใฎๆใฎ At(โ โ)
            
            if action == self.UP:
                print("โก๏ธ UP -> UP Rt = 1")
                self.Episode_1[2].append(1) # ไปใฏๆฌกใฎ่กๅใงๅฟใ็บ่ฆใงใใๅๆ(R = 1)
                print("Episode1 : {}".format(self.Episode_1))
                # self.Episode_2[2].append(random.choice([0, 1]))
            else:
                self.Episode_1[2].append(0)

        return self.Episode_0, self.Episode_1, self.Episode_2, self.Episode_3




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    X = [UP, DOWN, LEFT, RIGHT] # At-1
    A = [UP, DOWN, LEFT, RIGHT] # At
    R = [0, 1]

    # ็ฎๅฐใ็บ่ฆใใฆใใ้ใใฏ่กๅใ็ถ็ถใใฆใใ(ใคใพใใๆช็บ่ฆใซใชใฃใฆๅใใฆๆนๅใๅคใใ)ใจไปฎๅฎใใใจใAt-1ใงๆปใๆใใใฎๅใฎAt-2ใๆปใๆนๅใจๅใ
    
    V_0_LIST = []
    V_1_LIST = []
    V_2_LIST = []
    V_3_LIST = []
    RESULT = []

    data = []
    


    print("\n------------START------------\n")
    # ใณใใใฏใใผใฟใใใจใซ่กๅใใฉใฎใใใซใชใใใฎๅฎ้จ
                
    agent = Agent()

    ################
    " add test "
    prev_action = 2 #1 # -1
    # ๐ใใใ่จญๅฎ
    ################

    for epoch in range(1, 5): # 50):
        print("\n-----------{}steps------------\n".format(epoch))

        # prev_action = random.choice(X)
        
        ave_0, ave_1, ave_2, ave_3 = agent.value()
        
        V_0_LIST.append(ave_0)
        V_1_LIST.append(ave_1)
        V_2_LIST.append(ave_2)
        V_3_LIST.append(ave_3)

        action = agent.policy(prev_action, ave_0, ave_1, ave_2, ave_3) #, A_0, A_1, A_2, A_3)


        if action==  2:
            NEXT = "LEFT  โฌ๏ธ"
            print("    At :-> {}".format(NEXT))
        if action == -2:
            NEXT = "RIGHT โก๏ธ"
            print("    At :-> {}".format(NEXT))  
        if action ==  1:
            NEXT = "UP    โฌ๏ธ"
            print("    At :-> {}".format(NEXT))
        if action == -1:
            NEXT = "DOWN  โฌ๏ธ"
            print("    At :-> {}".format(NEXT))
        

        # print("\n---------- โ ๏ธ {}่ฉฆ่กๅพใฎ็ตๆ----------".format(5*epoch))
        print("\n---------- โ ๏ธ  {}่ฉฆ่กๅพใฎ็ตๆ----------".format(epoch))
        print("้ๅปใฎใจใใฝใผใใใใ็พๆ็นใงใฏใAt-1ใฎๆใAtใ้ธๆใใ")
        # Z = ้กไผผใจใใฝใผใ
        
        "test0824"
        # Add Episode ใใคใฉใฎ่กๅใๅใฃใใใฉใฎใใใๅ ฑ้ฌใๅพใใใใ
        print("\n----- โ ๏ธ  prev action = {}, action = {} -----".format(prev_action, action))
        
        print("๐ action = {}".format(action))
        
        action = action
        
        Episode_0, Episode_1, Episode_2, Episode_3 = agent.save_episode(prev_action, action)



        # print("---------- ๐ Episode_2 : {}----------".format(Episode_2))
        # print("---------- ๐ Episode_3 : {}----------".format(Episode_3))
        # print("---------- ๐ Episode_0 : {}----------".format(Episode_0))
        # print("---------- ๐ Episode_1 : {}----------".format(Episode_1))

        data.append(action)
        
    print("\n---------- โ ๏ธ  ่ฉฆ่ก็ตไบ----------")
    
    print("ๅนณๅไพกๅค[ๅทฆใใNๅ็ฎ]\n")
    print("V_0(โฌ๏ธ โก๏ธ ) : {}".format(V_0_LIST))
    print("V_1(โฌ๏ธ โก๏ธ ) : {}".format(V_1_LIST))
    print("V_2(โฌ๏ธ โฌ๏ธ ) : {}".format(V_2_LIST))
    print("V_3(โฌ๏ธ โฌ๏ธ ) : {}".format(V_3_LIST))

    # UPใไธ่ดใใฆใใSt
    if prev_action == 1:
        print("\nStใไธใใไธใซๆปใฃใฆใใๅ ดๅ")
        print("UP -> LEFT  : {}".format(data.count(2)))
        print("UP -> RIGHT : {}".format(data.count(-2)))
        
        RESULT.append(data.count(2))
        RESULT.append(data.count(-2))

    if prev_action == -1:
        print("\nStใไธใใไธใซๆปใฃใฆใใๅ ดๅ")
        print("DOWN -> LEFT  : {}".format(data.count(2)))
        print("DOWN -> RIGHT : {}".format(data.count(-2)))
        RESULT.append(data.count(2))
        RESULT.append(data.count(-2))

    if prev_action == 2:
        print("\nStใๅณใใๅทฆใซๆปใฃใฆใใๅ ดๅ")
        print("LEFT -> UP    : {}".format(data.count(1)))
        print("LEFT-> DOWN  : {}".format(data.count(-1)))
        RESULT.append(data.count(1))
        RESULT.append(data.count(-1))

    if prev_action == -1:
        print("\nStใๅทฆใใๅณใซๆปใฃใฆใใๅ ดๅ")
        print("RIGHT -> UP    : {}".format(data.count(1)))
        print("RIGHT -> DOWN  : {}".format(data.count(-1)))
        RESULT.append(data.count(1))
        RESULT.append(data.count(-1))

    print("RESULT:{}".format(RESULT))

main()

# ไธๅใ้ธๆใใใฆใใชใๆนๅใใใใจใจใฉใผใๅบใ