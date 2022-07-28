import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/


class Anim():
    # def __init__(self, STATE_HISTORY):
    def __init__(self):
        
        self.state_history = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 5], [2, 5], [2, 4], [2, 3], [2, 3], [2, 3], [2, 2], [2, 1], [2, 0], [2, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 1], [4, 2], [4, 2], [4, 2], [4, 3], [4, 4], [4, 5], [4, 5], [4, 4], [4, 3], [4, 2], [4, 2], [4, 2], [4, 1], [4, 0], [4, 0], [4, 0]]
        self.state_history = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 5], [2, 5], [2, 4], [2, 3], [2, 3], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 1], [4, 2], [4, 2], [4, 2], [4, 3], [4, 4], [4, 5], [4, 5], [4, 4], [4, 3], [4, 2], [4, 2], [4, 1], [4, 0], [4, 0]]


        # arr = np.array(self.state_history)
        # self.state_history = arr.flatten()
        print("STATE_HISTORY:{}".format(self.state_history))
        print(len(self.state_history))
        print(self.state_history[0][0])

        # self.data_change()

        self.fig = plt.figure(figsize=(7, 7))
        self.ax = plt.gca()
        self.ims = []

        self.view_plot_text()
        self.move_history()
        self.view_anim()

    # def data_change(self): # ここを別のリストに入れてみる
    #     for i in range(len(self.state_history)):
    #         if self.state_history[i] == 4:
    #             self.state_history[i] = 0
    #         elif self.state_history[i] == 5:
    #             self.state_history[i] = -1
    #         elif self.state_history[i] == 3:
    #             self.state_history[i] = 1
    #         elif self.state_history[i] == 2:
    #             self.state_history[i] = 2
    #         elif self.state_history[i] == 1:
    #             self.state_history[i] = 3
    #         print("Data Change !!")

        # return


    def view_plot_text(self):
        # 状態を示す文字S0～S8を描く
        plt.text(0.2, -0.5, ':(s0)', size=10, ha='center')
        plt.text(0.2, 1.5, 'S0', size=10, ha='center')
        plt.text(0.2, 3.5, 'S1', size=10, ha='center')
        plt.text(0.2, 5.5, 'S2', size=10, ha='center')
        plt.text(0.2, 7.5, 'S3', size=10, ha='center')
        plt.text(0.2, 9.5, 'S4', size=10, ha='center')
        plt.text(0.2, 11.5, 'S5', size=10, ha='center')
        # plt.text(0.8, 1.5, 'Branch', size=10, ha='center')
        plt.plot([0.5, 0.5], [0.0, 14.5], color="black")

        plt.plot([0.0, 10.5], [3.5, 3.5], color="black")
        plt.plot([0.0, 10.5], [7.5, 7.5], color="black")


        # plt.plot([0.5], [1.5], marker="s", color='black', markersize=40)
        # plt.plot([0.5], [3.5], marker="s", color='black', markersize=40)
        # plt.plot([0.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([0.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [11.5], marker="s", color='grey', markersize=40)
        # plt.plot([0.8], [1.5], marker="s", color='grey', markersize=40)

        
        
        plt.text(2.5, 3.5, 'S21', size=10, ha='center')
        plt.text(4.5, 3.5, 'S22', size=10, ha='center')
        plt.text(6.5, 3.5, 'S23', size=10, ha='center')
        plt.text(8.5, 3.5, 'S24', size=10, ha='center')
        plt.text(10.5, 3.5, 'S25', size=10, ha='center')

        plt.text(2.5, 7.5, 'S41', size=10, ha='center')
        plt.text(4.5, 7.5, 'S42', size=10, ha='center')
        plt.text(6.5, 7.5, 'S43', size=10, ha='center')
        plt.text(8.5, 7.5, 'S44', size=10, ha='center')
        plt.text(10.5, 7.5, 'S45', size=10, ha='center')

        plt.plot([2.5], [11.5], marker="s", color='black', markersize=40)
        plt.plot([4.5], [11.5], marker="s", color='black', markersize=40)
        plt.plot([6.5], [11.5], marker="s", color='black', markersize=40)
        plt.plot([8.5], [11.5], marker="s", color='black', markersize=40)
        plt.plot([10.5], [11.5], marker="s", color='black', markersize=40)
        
        plt.plot([2.5], [9.5], marker="s", color='black', markersize=40)
        plt.plot([4.5], [9.5], marker="s", color='black', markersize=40)
        plt.plot([6.5], [9.5], marker="s", color='black', markersize=40)
        plt.plot([8.5], [9.5], marker="s", color='black', markersize=40)
        plt.plot([10.5], [9.5], marker="s", color='black', markersize=40)

        plt.plot([2.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [7.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([4.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([6.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([8.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([10.5], [5.5], marker="s", color='black', markersize=40)

        plt.plot([2.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [3.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [1.5], marker="s", color='black', markersize=40)
        plt.plot([4.5], [1.5], marker="s", color='black', markersize=40)
        plt.plot([6.5], [1.5], marker="s", color='black', markersize=40)
        plt.plot([8.5], [1.5], marker="s", color='black', markersize=40)
        plt.plot([10.5], [1.5], marker="s", color='black', markersize=40)

        plt.plot([2.5], [-0.5], marker="s", color='black', markersize=40)
        plt.plot([4.5], [-0.5], marker="s", color='black', markersize=40)
        plt.plot([6.5], [-0.5], marker="s", color='black', markersize=40)
        plt.plot([8.5], [-0.5], marker="s", color='black', markersize=40)
        plt.plot([10.5], [-0.5], marker="s", color='black', markersize=40)

        # 描画範囲の設定と目盛りを消す設定
        # self.ax.set_xlim(0, 1)
        self.ax.set_xlim(-1.5, 12.5)
        self.ax.set_ylim(-1.5, 12.5)
        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')
        
        
    
    def move_history(self):
        line, = plt.plot([], [])
        self.ims.append([line])

        for t in range(len(self.state_history)): # フレームごとの描画内容
            
            # print("state history:{}".format(self.state_history))
            if t > 0:
                prev_state = state
            state = self.state_history[t]  # 現在の場所を描く
            try:
                print("next state")
                next_state = self.state_history[t+1]
            except:
                print("error")
                pass

            try:
                prev2 = self.state_history[t-1]
            except:
                pass
            print("STATE:{}".format(state))
            print("STATE[1]:{}".format(state[1]))

            if state[1] != 0:
                print("分岐")
                # x = 0.8
                # y = 1.5
                y = 13-(state[0] + state[0] + 1.5) #0.5
                x = state[1] + state[1] + 0.5
                # line, = plt.plot(x, y, marker="o", color='y', markersize=20)
            else:
                x = 0.5
                y = 13-(state[0] + state[0] + 1.5)

            # line, = plt.plot(x, y, marker="o", color='g', markersize=20)
            # line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)

            if state[0] > next_state[0] or state[1] > next_state[1]:
                print("!!!!!!!!!!!!")
            try:
                if state == prev_state:
                    # if state == next_state:
                    if state[0] < next_state[0] or state[1] > next_state[1]:
                        line, = plt.plot(x, y, marker="s", color='b', markersize=40, alpha = 0.5)
                        # pass
                    else:
                        line, = plt.plot(x, y, marker="s", color='y', markersize=40, alpha = 0.5)
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    # if state[0] < next_state[0] or state[1] > next_state[1]:
                    #     #     # print("!!!!!!!!!!!!!")
                    #     # if state == prev2:
                    #     #     print("prev2")
                    #     line, = plt.plot(x, y, marker="s", color='b', markersize=40, alpha = 0.5)
                    #     # pass
                    # else:
                    line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)
            except:
                print("エラー(初回)")
                line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)
            self.ims.append([line])
            if t == 0:
                self.ims.append([line])



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=250, repeat = True)
        plt.show()
        return True


if __name__ == "__main__":
    Anim()