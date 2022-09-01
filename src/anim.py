import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/

# animation_Edit.py の整理ver.

class Anim():
    
    def __init__(self, STATE_HISTORY):

        self.state_history = STATE_HISTORY
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = plt.gca()
        self.ims = []

    def view_plot_text(self):
        # 状態を示す文字S0～S8を描く
        plt.text(0.2, -0.5, 'S0', size=10, ha='center')
        plt.text(0.2, 1.5, 'S1', size=10, ha='center')
        plt.text(0.2, 3.5, 'S2', size=10, ha='center')
        plt.text(0.2, 5.5, 'S3', size=10, ha='center')
        plt.text(0.2, 7.5, 'S4', size=10, ha='center')
        plt.text(0.2, 9.5, 'S5', size=10, ha='center')
        plt.text(0.2, 11.5, 'S6', size=10, ha='center')
        
        plt.plot([0.5, 0.5], [0.0, 14.5], color="grey")
        plt.plot([0.0, 10.5], [1.5, 1.5], color="grey")
        # plt.plot([0.0, 10.5], [3.5, 3.5], color="grey")
        # plt.plot([0.0, 10.5], [7.5, 7.5], color="grey")
        
        plt.plot([0.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [11.5], marker="s", color='grey', markersize=40)

        plt.text(2.5, 1.5, 'S11', size=10, ha='center')
        plt.text(4.5, 1.5, 'S12', size=10, ha='center')
        plt.text(6.5, 1.5, 'S13', size=10, ha='center')
        plt.text(8.5, 1.5, 'S14', size=10, ha='center')
        plt.text(10.5, 1.5, 'S15', size=10, ha='center')
        
        plt.text(2.5, 3.5, 'S21', size=10, ha='center')
        plt.text(4.5, 3.5, 'S22', size=10, ha='center')
        plt.text(6.5, 3.5, 'S23', size=10, ha='center')
        plt.text(8.5, 3.5, 'S24', size=10, ha='center')
        plt.text(10.5, 3.5, 'S25', size=10, ha='center')

        plt.text(2.5, 5.5, 'S31', size=10, ha='center')

        plt.text(2.5, 7.5, 'S41', size=10, ha='center')
        plt.text(4.5, 7.5, 'S42', size=10, ha='center')
        plt.text(6.5, 7.5, 'S43', size=10, ha='center')
        plt.text(8.5, 7.5, 'S44', size=10, ha='center')
        plt.text(10.5, 7.5, 'S45', size=10, ha='center')

        plt.text(2.5, 9.5, 'S51', size=10, ha='center')

        plt.text(2.5, 11.5, 'S61', size=10, ha='center')

        # plt.text(2.5, 13.5, 'S71', size=10, ha='center')

        plt.plot([2.5], [11.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [11.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [11.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [11.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [11.5], marker="s", color='grey', markersize=40)
        
        plt.plot([2.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [9.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [9.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [7.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [7.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [5.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [3.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [1.5], marker="s", color='grey', markersize=40)

        plt.plot([2.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([4.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([6.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([8.5], [-0.5], marker="s", color='grey', markersize=40)
        plt.plot([10.5], [-0.5], marker="s", color='grey', markersize=40)

        # 描画範囲の設定と目盛りを消す設定
        
        self.ax.set_xlim(-1.5, 12.5)
        self.ax.set_ylim(-1.5, 12.5)
        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')
        
        
    
    def move_history(self):
        line, = plt.plot([], [])
        self.ims.append([line])

        for t in range(len(self.state_history)): # フレームごとの描画内容
            
            state = self.state_history[t]  # 現在の場所を描く
            
            try:
                next_state = self.state_history[t+1]
            except:
                pass

            try:
                prev_state = self.state_history[t-1]
            except:
                pass

            try:
                prev2 = self.state_history[t-2]
            except:
                pass
            

            if state[1] != 0:
                y = 13-(state[0] + state[0] + 1.5)
                x = state[1] + state[1] + 0.5
            else:
                x = 0.5
                y = 13-(state[0] + state[0] + 1.5)

            

            
            try:
                if state == prev_state:
                    
                    if state[0] < next_state[0] or state[1] > next_state[1]:
                        line, = plt.plot(x, y, marker="s", color='b', markersize=40, alpha = 0.5)
                    else:
                        # if prev_state[0] > prev2[0] or prev_state[1] < prev2[1]:
                            # line, = plt.plot(x, y, marker="s", color='b', markersize=40, alpha = 0.5)
                        # else:
                        if state[0] == prev_state[0] == prev2[0] or state[0] == prev_state[0] == next_state[0]:
                            line, = plt.plot(x, y, marker="s", color='y', markersize=40, alpha = 0.5)
                        else:
                            line, = plt.plot(x, y, marker="s", color='b', markersize=40, alpha = 0.5)
                else:
                    line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)
            except:
                print("エラー(初回)")
                line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)
            self.ims.append([line])
            if t == 0:
                self.ims.append([line])



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        # self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=200, repeat = False)
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=250, repeat = True)
        plt.show()
        return True


if __name__ == "__main__":

    
    
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3], [1, 3], [0, 3], [0, 3], [0, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0],         [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]

    # stressfull = 2
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [0, 2], [0, 2], [1, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [0, 3], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [4, 2], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 2], [5, 1], [5, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 2], [4, 2], [4, 1], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 2], [3, 2], [3, 1]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [2, 1], [3, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [2, 1], [3, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 3], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 2], [2, 2], [1, 2], [1, 2], [2, 2], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [1, 1], [1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1], [4, 0], [4, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [1, 3]]
    
    # 0821
    STATE_HISTORY = [[6, 2], [5, 2], [5, 2]]
    STATE_HISTORY = [[6, 2], [5, 2], [5, 2], [5, 2], [4, 2], [4, 2], [4, 2], [3, 2], [3, 2], [4, 2], [4, 2], [4, 2], [4, 2], [4, 3], [4, 3], [4, 2], [4, 2], [4, 2], [4, 2], [3, 2], [3, 2], [4, 2], [5, 2], [5, 2], [5, 2], [5, 2], [5, 3], [5, 3], [5, 2]]
    STATE_HISTORY = [[5, 2], [4, 2], [4, 2], [4, 2], [3, 2], [3, 2], [4, 2], [4, 2], [4, 2], [4, 2], [4, 3], [4, 3], [4, 2]]




    Env_Anim = Anim(STATE_HISTORY)

    print("STATE_HISTORY:{}".format(Env_Anim.state_history))
    print("length:{}".format(len(Env_Anim.state_history)))

    Env_Anim.view_plot_text()
    Env_Anim.move_history()
    Env_Anim.view_anim()

    