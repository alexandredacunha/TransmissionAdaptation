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
