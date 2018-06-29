"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the environment part of this example. The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""


import numpy as np
import time
import sys
from dogleg import *

#if sys.version_info.major == 2:
#    import Tkinter as tk
#else:
#    import tkinter as tk

# UNIT = 40   # pixels
# MAZE_H = 4  # grid height
# MAZE_W = 4  # grid width

class DogeMovement(object):
    """docstring for DogeMovement."""
    def __init__(self):
        super(DogeMovement, self).__init__()
        self.action_space = ['straight', 'left_turn', 'right_turn']
        self.n_actions = len(self.action_space)
        # self.initialPose = np.array([[0],[0]])
        # self.title('dogleg')
    def reset(self):
        #self.update()
        time.sleep(1)
        motorangle(0)
        # hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
        # degreeinit, minutesinit = hmc5883l.getHeading()
        # return self.canvas.coords(self.rect)

    def step(self, action):
        # degree, minutes = i2c_hmc5883l.getHeading()
        # degreefixed = degree - degreeinit
        # s = self.canvas.coords(self.rect)
        s = [obstacle_distance(), getAcc()[1], isarrived()] # store previous observation
        # take an action
        if action == 0:   # straight
            print('straight')
            motorangle(0)
        elif action == 1:   # small_left_turn
            print('left')
            motorangle(1)
        elif action == 2:   # small_right_turn
            print('right')
            motorangle(2)
        # get observation after taken action
        s_ = [obstacle_distance(), getAcc()[1], isarrived()]
        print("s_")
        print(s_)
        # reward function
        if s_[2]:
            reward = 1
            done = True
            s_ = 'terminal'
            print("Congratulations!")
        elif s_[0] <= 15: #or s_[1] < 0.014: # cant get steps
            reward = -1
            done = True
            s_ = 'terminal'
            print("episode done bcz meeting obstacle")
        else:
            reward = 0.01*(50-s_[0])
            done = False

        return s_, reward, done

    def render(self):
        time.sleep(0.1)
        #self.update()

def update(self):
    for t in range(10):
    #   s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = DogeMovement()
    update()
#    env.after(100,update)
#    env.mainloop()
