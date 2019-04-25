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
import visualizerEngineMatplotlib as visualizerEngine
from packetsizecalculator.DQNAgent import DQNAgent
from packetsizecalculator.DQNAgent import MINI_BATCH_SIZE

DEFAULT_SIZE = 1000
MAX_SIZE = 1000
MIN_SIZE = 0

class PacketSizeEstimatorBase():
    """Base class for packet size estimator"""
    def __init__(self):
        self.channel_quality_reported_prev = None
        self.channel_quality_reported = None
        self.transmission_results = 0    # ack = 1; nack = 0
        self.score = 0

    @abstractmethod
    def get_optimal_size_for_next_tx(self, time):
        pass
        
    def store_last_tx_result(self, acknack, cqi):
        pass


class FixedPacketSize(PacketSizeEstimatorBase):
    """fixed packet size estimator"""
    def __init__(self):
        super(FixedPacketSize, self).__init__()
        self.packet_size = DEFAULT_SIZE

    def get_optimal_size_for_next_tx(self, time):
        return self.packet_size


class SimpleEstimator(PacketSizeEstimatorBase):
    """simple packet size estimator"""
    def __init__(self):
        super(SimpleEstimator, self).__init__()
        self.packet_size = DEFAULT_SIZE/2
        self._up_rate = 50
        self._down_rate = 50
        self.calculated_sizes = []

    def get_optimal_size_for_next_tx(self, time):
        self.store_sizes()
        return self.packet_size

    def store_last_tx_result(self, acknack, cqi):
        if acknack == "ACK":
            self.packet_size = min(self.packet_size + self._up_rate, MAX_SIZE)
            print(self.packet_size)
        if acknack == "NACK":
            self.packet_size = max(self.packet_size - self._down_rate, MIN_SIZE)
            print(self.packet_size)
            
    def store_sizes(self):
        self.calculated_sizes.append(self.packet_size)
        
    def plot_calculated_sizes(self):
        print(self.calculated_sizes)
        visualizerEngine.PlotXYgraph(
            title = "sizes", 
            vector = self.calculated_sizes)


class DQNEstimator_3_actions(PacketSizeEstimatorBase):
    """simple packet size estimator"""
    def __init__(self):
        super(DQNEstimator_3_actions, self).__init__()
        self.packet_size = DEFAULT_SIZE/2
        self._up_rate = 10
        self._down_rate = 10
        self.calculated_sizes = []
        self.dqn_agent = DQNAgent(4,3)

        self._prev_state = None
        self._prev_action = None

    def get_optimal_size_for_next_tx(self, time):
        print("time {}".format(time))
        reward = (self.transmission_results * self.packet_size)
        print("reward {}".format(reward))
        state = np.array([self.channel_quality_reported_prev,
                 self.channel_quality_reported,
                 self.transmission_results,
                 self.packet_size])
        state = np.reshape(state, [1, 4])
        if (self._prev_action != None): # not store first time 
            self.dqn_agent.store_transition_in_D(self._prev_state, 
                                                 self._prev_action, 
                                                 reward,
                                                 state)
        if len(self.dqn_agent.memory_D) > MINI_BATCH_SIZE:
            self.dqn_agent.replay(MINI_BATCH_SIZE)
        # calculate best action from model
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
            self.transmission_results = 1
        if acknack == "NACK":
            self.transmission_results = 0
            
    def store_sizes(self):
        self.calculated_sizes.append(self.packet_size)
        
    def plot_calculated_sizes(self):
        print(self.calculated_sizes)
        visualizerEngine.PlotXYgraph(
            title = "sizes", 
            vector = self.calculated_sizes)
