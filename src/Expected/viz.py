from turtle import color
import numpy as np
import matplotlib.pyplot as plt
 

class Illustration():

    def __init__(self):

        # self.x = [1, 2, 3, 4, 5, 6, 7, 8]
        # self.x = ["⇧ ⇦", "⇧ ⇨", "⇩ ⇦", "⇩ ⇨", "⇦ ⇧", "⇦ ⇩", "⇨ ⇧", "⇨ ⇩"]

        self.x = [1, 2, None, 0]
        
        self.y = ["lost", "A", "B", "C"]

        self.x2 = [0, 1, 2,    3,4,5,6,7,8]
        self.y2 = [3, 0, 1,    1,0,3,3,0,2]

        self.x3 = [0, 1, 2]

        # self.y3 = [3, 0, 2]
        self.y3 = [1, 0, 2]
        self.y4 = [2, 0, 1]
        self.y5 = [1, 0, 3]

        # self.view_bar()
        self.view_plot()

    def view_bar(self):
        plt.scatter(self.x, self.y, color="orange")
        # plt.bar(self.x, self.y, color="red")
        plt.show()

    def view_plot(self):
        # plt.plot(self.x2, self.y2, color="orange", marker = "o")

        plt.title("Graph of lost/choice")
        plt.xlabel("t")
        # plt.ylabel("Ignited NODE Location")
        plt.ylabel("State")
        plt.ylim(0, 3)

        plt.plot(self.x3, self.y3, label = "1試行目",color="green", marker = "o", alpha=0.5)
        # plt.plot(self.x3, self.y4, label = "2試行目",color="blue", marker = "o", alpha=0.5)
        # plt.plot(self.x3, self.y5, label = "3試行目",color="green", marker = "o", alpha=0.5)

        plt.legend()
        plt.grid()
        plt.show()


Illustration()