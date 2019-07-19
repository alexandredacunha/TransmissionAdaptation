#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  packetSizeEstimatorBase.py
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

from abc import ABCMeta, abstractmethod
import numpy as np
import visualizationtools.visualizerEngineMatplotlib as visualizerEngine
from packetsizecalculator.DQNAgent import DQNAgent
from packetsizecalculator.DQNAgent import MINI_BATCH_SIZE
from packetsizecalculator.packetSizeEstimator import PacketSizeEstimatorBase

DEFAULT_SIZE = 1000/2
MAX_SIZE = 1000
MIN_SIZE = 0
ACK = 1
NACK = -1


class DQNEstimator_3_actions(PacketSizeEstimatorBase):
    """simple packet size estimator"""
    def __init__(self):
        super(DQNEstimator_3_actions, self).__init__()
        self.packet_size = DEFAULT_SIZE
        self._up_rate = 50
        self._down_rate = 50
        self.calculated_sizes = []
        self.dqn_agent = DQNAgent(state_size = 4, action_size = 3)

        self._prev_state = None
        self._prev_action = None

    def get_optimal_size_for_next_tx(self, time):
        if self.channel_quality_reported_prev == None or \
           self.channel_quality_reported == None or \
           self.transmission_results == None:
            return self.packet_size
        print("time {}".format(time))
        reward = (self.transmission_results * self.packet_size)/100
        print("reward {}".format(reward))
        state = np.array([self.channel_quality_reported_prev,
                 self.channel_quality_reported,
                 self.transmission_results,
                 self.packet_size])
        state = np.reshape(state, [1, 4])
        if self._prev_action != None:
            self.dqn_agent.store_transition_in_D(self._prev_state, 
                                                self._prev_action, 
                                                reward,
                                                state)
        if (self.dqn_agent.memory_D.get_size()) > 100:
            self.dqn_agent.replay(MINI_BATCH_SIZE)
        # calculate best action from model
        print("CQI: " + str(self.channel_quality_reported))
        action = self.dqn_agent.act(state)
        if action == 0:
            pass # do nothing
        elif action == 1:
            self.packet_size = max(self.packet_size - self._down_rate, MIN_SIZE)
        elif action == 2:
            self.packet_size = min(self.packet_size + self._up_rate, MAX_SIZE)    
        
        # keep state, action, reward to store in memory D when new state received
        self._prev_state = state
        self._prev_action = action
        print("packet size: {}".format(self.packet_size))

        self.store_sizes()
        return self.packet_size

    def store_last_tx_result(self, acknack, cqi):
        if self.channel_quality_reported != None:
            self.channel_quality_reported_prev = self.channel_quality_reported
        else:
            self.channel_quality_reported_prev = cqi # avoid init errors
        self.channel_quality_reported = cqi
        if acknack == "ACK":
            self.transmission_results = ACK
        if acknack == "NACK":
            self.transmission_results = NACK
            
    def store_sizes(self):
        self.calculated_sizes.append(self.packet_size)
        
    def plot_calculated_sizes(self):
        print(self.calculated_sizes)
        visualizerEngine.PlotXYgraph(
            title = "sizes", 
            vector = self.calculated_sizes)
