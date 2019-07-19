#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DQNAgent.py
#  
#  Copyright 2018 Alex C <dacunha.alexandre@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import visualizationtools.visualizerEngineMatplotlib as visualizerEngine
from abc import ABCMeta, abstractmethod
import random
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

MINI_BATCH_SIZE = 32
REPLAY_MEMORY_SIZE = 2000
AGENT_HISTORY_LENGTH = 1 # not used
TARGET_NETWORK_UPDATE_FREQUENCY = 100000 # not used
DISCOUNT_FACTOR = 0.99
ACTION_REPEAT = 4 # not used
LEARNING_RATE = 0.005
GRADIENT_MOMENTUM = 0.95 # not used
SQUARED_GRADIENT_MOMENTUM = 0.95 # not used
MIN_SQUARED_GRADIENT = 0.01 # not used
INITIAL_EXPLORATION = 1.0
FINAL_EXPLORATION = 0.1
FINAL_EXPLORATION_STEP = 1000
REPLAY_START_SIZE = 100
NO_OP_MAX = 30 # not used


class ReplayMemoryBase():
    @abstractmethod
    def __init__(self, memory_size):
        pass
    
    @abstractmethod
    def store_replay_data(self, state, action, reward, next_state):
        pass
    
    @abstractmethod
    def sample_minibatch(self, batch_size):
        pass

    @abstractmethod
    def get_size(self):
        return 0

class DQNAgent():
    """fixed packet size estimator"""
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory_D = ReplayMemoryDeque(REPLAY_MEMORY_SIZE) # D
        self.gamma = DISCOUNT_FACTOR # importance of future rewards
        self.epsilon_greedy = INITIAL_EXPLORATION # exploration rate
        self.epsilon_decay = pow(FINAL_EXPLORATION, 1.0/FINAL_EXPLORATION_STEP)
        self.epsilon_min = FINAL_EXPLORATION 
        self.learning_rate = LEARNING_RATE
        self.Q_function_NN = self._build_Q_value_function_NN()
        
    def _build_Q_value_function_NN(self):
        mlp = Sequential()
        mlp.add(Dense(12, input_dim=self.state_size, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        mlp.add(Dense(12, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        mlp.add(Dense(self.action_size, activation='linear'))
        mlp.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return mlp
        
    def store_transition_in_D(self, state, action, reward, next_state):
        #self.memory_D.append((state, action, reward, next_state))
        self.memory_D.store_replay_data(state, action, reward, next_state)
        
    def act(self, state):
        # with probability epsilon_greedy choose random action for exploring environment
        if np.random.rand() <= self.epsilon_greedy:
            exploration_action = random.randrange(self.action_size)
            return exploration_action
        print("EXPLOIT!!!!")
        exploitation_action_from_Q = self.Q_function_NN.predict(state)[0]
        print(exploitation_action_from_Q)
        action_corresponding_max_predicted_reward = np.argmax(exploitation_action_from_Q)
        print("action " + str(action_corresponding_max_predicted_reward))
        return action_corresponding_max_predicted_reward
        
    def replay(self, batch_size):
        #sample_minibatch_from_memory_D = random.sample(self.memory_D, batch_size)
        sample_minibatch_from_memory_D = self.memory_D.sample_minibatch(batch_size)
        for state, action, reward, next_state in sample_minibatch_from_memory_D:
            print("-----------")
            print("state: " + str(state))
            print("action: " + str(action))
            print("reward: " + str(reward))
            #print(next_state)
            target_y = reward 
            done = False 
            if not done: # estimate future rewards always in our case, game does not end
                reward_in_next_state_when_optimal_action_taken = np.amax(self.Q_function_NN.predict(next_state)[0])
                target_y = (reward + self.gamma * reward_in_next_state_when_optimal_action_taken)
            Q_state_action = self.Q_function_NN.predict(state)
            print("predicted state: " + str(Q_state_action))
            # correct the output state with what would be the real reward from 
            # experience when having selecting the "action" and predicted future reward
            Q_state_action[0][action] = target_y 
            print("expected: " + str(Q_state_action))

            Q_state_action = normalize(Q_state_action)
            print("expected Norm : " + str(Q_state_action))
            # gradient descent giving calculated above rewards array as training data
            self.Q_function_NN.fit(state, Q_state_action, epochs=1, verbose=0) 
        if self.epsilon_greedy > self.epsilon_min:
            self.epsilon_greedy *= self.epsilon_decay

    def load(self, name):
        self.Q_function_NN.load_weights(name)

    def save(self, name):
        self.Q_function_NN.save_weights(name)

        
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm


class ReplayMemoryDeque(ReplayMemoryBase):
    def __init__(self, memory_size):
        self.memory_D = deque(maxlen = memory_size)
    
    def store_replay_data(self, state, action, reward, next_state):
        self.memory_D.append((state, action, reward, next_state))
    
    def sample_minibatch(self, batch_size):
        return random.sample(self.memory_D, batch_size)

    def get_size(self):
        return len(self.memory_D)


class ReplayMemoryDictionary(ReplayMemoryBase):
    def __init__(self, memory_size):
        self.memory_D = deque(maxlen = memory_size)
    
    def store_replay_data(self, state, action, reward, next_state):
        self.memory_D.append((state, action, reward, next_state))
    
    def sample_minibatch(self, batch_size):
        return random.sample(self.memory_D, batch_size)

    def get_size(self):
        return len(self.memory_D)
