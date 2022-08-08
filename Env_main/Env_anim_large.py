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
        plt.text(0.5, -0.5, 'S0', size=8, ha='center')
        plt.text(0.5, 1.5, 'S1', size=8, ha='center')
        plt.text(0.5, 3.5, 'S2', size=8, ha='center')
        plt.text(0.5, 5.5, 'S3', size=8, ha='center')
        plt.text(0.5, 7.5, 'S4', size=8, ha='center')
        plt.text(0.5, 9.5, 'S5', size=8, ha='center')
        plt.text(0.5, 11.5, 'S6', size=8, ha='center')
        plt.text(0.5, 13.5, 'S7', size=8, ha='center')
        plt.text(0.5, 15.5, 'S8', size=8, ha='center')
        plt.text(0.5, 17.5, 'S9', size=8, ha='center')
        plt.text(0.5, 19.5, 'S10', size=8, ha='center')
        
        plt.plot([0.5, 0.5], [0.0, 20.5], color="black")
        plt.plot([0.0, 20.5], [1.5, 1.5], color="black")
        plt.plot([0.0, 20.5], [3.5, 3.5], color="black")
        plt.plot([0.0, 20.5], [7.5, 7.5], color="black")
        
        plt.plot([0.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([0.5], [21.5], marker="s", color='grey', markersize=25)

        # plt.text(2.5, 1.5, 'S11', size=8, ha='center')
        # plt.text(4.5, 1.5, 'S12', size=8, ha='center')
        # plt.text(6.5, 1.5, 'S13', size=8, ha='center')
        # plt.text(8.5, 1.5, 'S14', size=8, ha='center')
        # plt.text(10.5, 1.5, 'S15', size=8, ha='center')
        # plt.text(12.5, 1.5, 'S16', size=8, ha='center')
        # plt.text(14.5, 1.5, 'S17', size=8, ha='center')
        # plt.text(16.5, 1.5, 'S18', size=8, ha='center')
        # plt.text(18.5, 1.5, 'S19', size=8, ha='center')
        
        # plt.text(2.5, 3.5, 'S21', size=8, ha='center')
        # plt.text(4.5, 3.5, 'S22', size=8, ha='center')
        # plt.text(6.5, 3.5, 'S23', size=8, ha='center')
        # plt.text(8.5, 3.5, 'S24', size=8, ha='center')
        # plt.text(10.5, 3.5, 'S25', size=8, ha='center')
        # plt.text(12.5, 3.5, 'S26', size=8, ha='center')
        # plt.text(14.5, 3.5, 'S27', size=8, ha='center')
        # plt.text(16.5, 3.5, 'S28', size=8, ha='center')
        # plt.text(18.5, 3.5, 'S29', size=8, ha='center')

        # plt.text(2.5, 7.5, 'S41', size=8, ha='center')
        # plt.text(4.5, 7.5, 'S42', size=8, ha='center')
        # plt.text(6.5, 7.5, 'S43', size=8, ha='center')
        # plt.text(8.5, 7.5, 'S44', size=8, ha='center')
        # plt.text(10.5, 7.5, 'S45', size=8, ha='center')
        # plt.text(12.5, 7.5, 'S46', size=8, ha='center')
        # plt.text(14.5, 7.5, 'S47', size=8, ha='center')
        # plt.text(16.5, 7.5, 'S48', size=8, ha='center')
        # plt.text(18.5, 7.5, 'S49', size=8, ha='center')

        plt.plot([2.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [11.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [11.5], marker="s", color='grey', markersize=25)
        
        plt.plot([2.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [9.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [9.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [7.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [7.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [5.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [5.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [3.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [3.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [1.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [1.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [-0.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [-0.5], marker="s", color='grey', markersize=25)



        plt.plot([2.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [13.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [13.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [15.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [15.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [17.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [17.5], marker="s", color='grey', markersize=25)

        plt.plot([2.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([4.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([6.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([8.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([10.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([12.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([14.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([16.5], [19.5], marker="s", color='grey', markersize=25)
        plt.plot([18.5], [19.5], marker="s", color='grey', markersize=25)

        # 描画範囲の設定と目盛りを消す設定
        
        self.ax.set_xlim(-1.5, 20.5)
        self.ax.set_ylim(-1.5, 20.5)
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
                y = 21-(state[0] + state[0] + 1.5)
                x = state[1] + state[1] + 0.5
            else:
                x = 0.5
                y = 21-(state[0] + state[0] + 1.5)


            plt.title('State[{}], Steps={}'.format(self.state_history[t], t))

            

            
            try:
                if state == prev_state:
                    
                    if state[0] < next_state[0] or state[1] > next_state[1]:
                        line, = plt.plot(x, y, marker="s", color='b', markersize=25, alpha = 0.5)
                    else:
                        if prev_state[0] > prev2[0] or prev_state[1] < prev2[1]:
                            line, = plt.plot(x, y, marker="s", color='b', markersize=25, alpha = 0.5)
                        else:
                            line, = plt.plot(x, y, marker="s", color='y', markersize=25, alpha = 0.5)
                else:
                    line, = plt.plot(x, y, marker="s", color='r', markersize=25, alpha = 0.5)
            except:
                print("エラー(初回)")
                line, = plt.plot(x, y, marker="s", color='r', markersize=25, alpha = 0.5)
            self.ims.append([line])
            if t == 0:
                self.ims.append([line])



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=200, repeat = False)
        plt.show()
        return True


if __name__ == "__main__":

    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 1], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 2], [5, 1], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 3], [5, 2], [5, 1], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0]]

    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 3], [5, 2], [5, 1], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 3], [5, 2], [5, 1], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1]]

    # Δs = 0
    STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 1], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 3], [5, 2], [5, 1], [5, 0], [5, 0]]
    # Δs = -1
    # STATE_HISTORY = [[6, 0], [5, 0], [5, 0], [5, 0], [4, 0], [3, 0], [2, 0], [2, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [2, 2], [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 2], [2, 1], [2, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 3], [5, 2], [5, 1], [5, 0], [5, 0]]
    # ADD
    STATE_HISTORY = [[10, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [4, 0], [5, 0], [6, 0], [6, 0], [6, 1], [6, 2], [6, 2], [6, 2], [6, 3], [6, 4], [6, 4], [6, 3], [6, 2], [6, 2], [6, 1], [6, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 3], [9, 2], [9, 1], [9, 0], [9, 0]]
    STATE_HISTORY = [[10, 0], [9, 0], [9, 0], [9, 0], [8, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 2], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [4, 0], [5, 0], [6, 0], [6, 0], [6, 1], [6, 2], [6, 2], [6, 2], [6, 3], [6, 4], [6, 4], [6, 3], [6, 2], [6, 2], [6, 1], [6, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 3], [9, 2], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [1, 0], [1, 0], [2, 0], [3, 0], [3, 0], [3, 1], [3, 2], [3, 2], [3, 1], [3, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 0], [6, 1], [6, 2], [6, 2], [6, 2], [6, 3], [6, 4], [6, 5], [6, 5], [6, 5], [6, 6], [6, 7], [6, 8], [6, 8], [6, 7], [6, 6], [6, 5], [6, 5], [6, 4], [6, 3], [6, 2], [6, 2], [6, 1], [6, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 4], [9, 3], [9, 2], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [1, 0], [0, 0], [0, 0], [1, 0], [2, 0], [3, 0], [3, 0], [3, 1], [3, 2], [3, 3], [3, 3], [3, 2], [3, 1], [3, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 0], [6, 1], [6, 2], [6, 2], [6, 2], [6, 3], [6, 4], [6, 5], [6, 5], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 9], [6, 8], [6, 7], [6, 6], [6, 5], [6, 5], [6, 4], [6, 3], [6, 2], [6, 2], [6, 1], [6, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 5], [9, 4], [9, 3], [9, 2], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [2, 0], [3, 0], [3, 0], [3, 1], [3, 2], [3, 3], [3, 3], [3, 2], [3, 1], [3, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 0], [6, 1], [6, 2], [6, 2], [6, 2], [6, 3], [6, 4], [6, 5], [6, 5], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 9], [6, 8], [6, 7], [6, 6], [6, 5], [6, 5], [6, 4], [6, 3], [6, 2], [6, 2], [6, 1], [6, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 6], [9, 5], [9, 4], [9, 3], [9, 2], [9, 1], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [8, 0], [7, 0], [6, 0], [6, 0], [6, 0], [5, 0], [4, 0], [3, 0], [3, 0], [3, 0], [2, 0]]
    Env_Anim = Anim(STATE_HISTORY)

    print("STATE_HISTORY:{}".format(Env_Anim.state_history))
    print("length:{}".format(len(Env_Anim.state_history)))

    Env_Anim.view_plot_text()
    Env_Anim.move_history()
    Env_Anim.view_anim()

    