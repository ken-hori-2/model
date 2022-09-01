from turtle import color
import numpy as np
import matplotlib.pyplot as plt
 

class Illustration():

    def __init__(self):

        self.x = [1, 2, 3, 4, 5, 6, 7, 8]
        self.x = ["⇧ ⇦", "⇧ ⇨", "⇩ ⇦", "⇩ ⇨", "⇦ ⇧", "⇦ ⇩", "⇨ ⇧", "⇨ ⇩"]
        
        self.y = [233, 267, 258, 242, 487, 13, 500, 0]
        self.y = [254, 246, 254, 246, 498, 2, 496, 4]
        self.y = [257, 243, 259, 241, 499, 1, 492, 8]

        # self.x = [1, 2]
        # self.x = ["⇦", "⇨"]
        # self.y = [23, 27]
        # self.y = [26,24]

        # self.x = ["⇧", "⇩"]
        # # self.y = [48,2]
        # self.y = [46,4]
        
        self.view_bar()
        # self.view_plot()

    def view_bar(self):
        plt.bar(self.x, self.y, color="orange")
        # plt.bar(self.x, self.y, color="red")
        plt.show()

    def view_plot(self):
        plt.plot(self.y, color="orange")
        plt.show()


Illustration()