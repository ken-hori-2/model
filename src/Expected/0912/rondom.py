import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML

W = 500#回数
step = np.random.choice([-1,1],W) # -1 or 1 をチョイスしたL個の配列生成
position = np.cumsum(step)  #累積和    

fig, ax = plt.subplots()
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
x=np.arange(0,W,1)
ax.plot(x,position,"C2o-",alpha=0.5)
fig.savefig("1Drandomwalk.png", dpi=100,transparent = False, bbox_inches = 'tight')
plt.show()


#Animation
fig, ax = plt.subplots(figsize=(6,4))
p1, = ax.plot([], [],'-o',color='C2',alpha=0.5)


def update(i):
    p1.set_data((x[:i],position[:i]))
    ax.set_xlim(0,x[i+1])
    ax.set_ylim(position.min(),position.max())    
    return fig,

ani = animation.FuncAnimation(fig, update, 499,interval=20, blit=True)
ani.save('rw1d_anim.gif', writer="ffmpeg",dpi=100)
# HTML(ani.to_html5_video())
# plt.show()