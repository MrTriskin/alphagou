"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import DogeMovement
from RL_brain import QLearningTable
from dogleg import *

import pandas as pd

def update():
    actiontable=[]
    observation_table=[]
    observationtable=[]
    rewardtable=[]
    timestable =[]

    for episode in range(100):
        print("episode %.1f completed" % episode)
        time.sleep(10)
        # initial observation
        observation = env.reset()
        times = 0
        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            observation = observation_
            times += times
            
            actiontable.append(action)
            observation_table.append(observation_)
            observationtable.append(observation)
            rewardtable.append(reward)
            timestable.append(times)
#            print(actiontable)
#            print(rewardtable)
            # break while loop when end of this episode
            if done:

                actiontable.append(-100)
                observation_table.append([-100,-100,-100])
                observationtable.append([-100,-100,-100])
                rewardtable.append(-100)
                timestable.append(-100)

                break

    # end of game
    print('game over')
    my_action = pd.DataFrame(actiontable)
    my_observation_table = pd.DataFrame(observation_table)
    my_observationtable = pd.DataFrame(observationtable)
    my_reward = pd.DataFrame(rewardtable)
    my_times = pd.DataFrame(timestable)    
    RL.q_table.to_csv('q_table.csv')
    my_action.to_csv('action.csv')
    my_observation_.to_csv('observation_.csv')
    my_observation.to_csv('observation.csv')
    my_reward.to_csv('reward.csv')
    my_times.to_csv('times.csv')
    
    env.destroy()

if __name__ == "__main__":
    motorangle(0)
    
    env = DogeMovement()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    
    update()
        
#    env.after(100, update)
#    env.mainloop()
