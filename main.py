#Main_simple_now_0725.py　のbranch ver.

class algorithm():

    def __init__(self, s, stressfull):
        self.s = s
        self.max = stressfull
        self.trigar = False
        self.select_next_bp = False
        self.down = False
        self.afterdown = False
        self.branch = False
        self.save = False
        self.BPLIST = []
        
        self.NODELIST = [1, 1, 0, 0, 0, 0, 0]
        self.NODELIST = [1, 1, 1, 0, 0, 0, 0]
        self.NODELIST = [1, 1, 0, 1, 0, 0, 0]
        # self.NODELIST = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0]
        # self.NODELIST = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]

        
        self.next_bp = 0
        print("NODE LIST :{}".format(self.NODELIST))
    
    def model(self, delta_s, done, state, j, state_history):
        
        print("#########state:{}##########".format(state))
        if self.s < self.max:
            print("stress:{}".format(self.s))
            if self.NODELIST[state] == 1:
                print("Node発見")
                #########################
                self.BPLIST.append(state)
                # 一個前が1ならpopで削除
                print("削除前 {}".format(self.BPLIST))
                length = len(self.BPLIST)
                if self.NODELIST[state - 1] == 1 and length > 1:
                    self.BPLIST.pop(-2)
                    print("削除後 {}".format(self.BPLIST))
                print("storage  BPLIST:{}".format(self.BPLIST))
                #########################
                # state_history.append(state)                                       # comment out 0725
            elif self.NODELIST[state] == 0: 
                print("Node未発見")   
                self.s += delta_s
                print("stress:{}".format(self.s))


            if self.s >= self.max and not self.trigar:
                self.trigar = True
                self.select_next_bp = True
                print("stressfull")
                
                # return done, state ,j, state_history                              # comment out 0725



            state += 1
            print("################")
            
            # return done, state ,j, state_history                                  # comment out 0725
        

        
        

        if self.select_next_bp:
            self.select_next_bp = False
            self.down = True
            print("select next bp")
            
            try:
                self.next_bp = self.BPLIST[-j]
                print("[next bp : NODE {}]".format(self.next_bp))
            except:
                print("これ以上戻れません 終了します")
                
                # done = True  # ループさせない時はこれを戻す # コメントアウト0725
                state = self.next_bp
                j = 1
                self.down = False
                self.s = 0
                self.trigar = False
                self.BPLIST.clear()
                print("state, j = {},{} BP list:{}".format(state, j, self.BPLIST))
                
                print("[next bp : NODE {}]".format(self.next_bp))                   # tab 0725
                
                return done, state, j, state_history                                # tab 0725
        

        if self.down:
            self.down = False
            self.afterdown  = True
            print("On the way down")
            back_true = True
            while back_true:
                state -= 1
                print("-----------")
                print("[NODE {}]".format(state))
                if state == self.next_bp:
                    back_true = False
            print("-----------")
            
            # return done, state, j, state_history                                  # comment out 0725
        

        if self.afterdown:
            self.afterdown = False
            # self.branch = True  コメントアウト 0724
            print("Afterdown Decision Making")
            self.select_next_bp = True
            j += 1
        
        return done, state, j, state_history                                        # shift + tab 0725


if __name__ == "__main__":
    done = False
    s = 0
    stressfull = 3
    delta_s = 1

    Algo = algorithm(s, stressfull)
    
    count = 0
    state = 0
    j = 1

    state_history = []
    while not done:

        print("{} NODE {}".format(count, state))
        state_history.append(state)
        
        done , state , j , state_history= Algo.model(delta_s, done, state, j, state_history)

        print("⇩")

        count += 1


        if count > 30:
            done = True
            break

    print("state history : {}".format(state_history))
