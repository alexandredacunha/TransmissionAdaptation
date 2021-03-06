#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  channel.py
#  
#  Copyright 2018 cunha <dacunha.alexandre@gmail.com>
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
import queue
import inspect
import random
import numpy
from simulator import messages
import logging
import math
import visualizationtools.visualizerEngineMatplotlib as visualizerEngine

MAX_RATE_UP = 2.5
MAX_RATE_DOWN = 2.5

class Channel():
    """A class for """
    
    def __init__(self, simulation_length, csvfilelog = None):
        self._receiver_queue = queue.Queue()
        self._sender_queue = queue.Queue()
        self._observer_list = []
        self._max_time = simulation_length
        self._channel_quality_vector = numpy.full(self._max_time, 100)
        self._time = 0
        self._seed = 0
        self._instances_monitoring_time_list = []
        self._csvfile = None
        if csvfilelog != None:
            self._csvfile = open(csvfilelog, "w")

    def _get_caller_name(self):
        stack = inspect.stack()
        the_class = stack[2][0].f_locals["self"].__class__
        return str(the_class)
    
    def receive(self):
        caller_name = self._get_caller_name()
        if caller_name == "<class 'simulator.receiver.Receiver'>":
            queue = self._receiver_queue
        elif caller_name == "<class 'simulator.sender.Sender'>":
            queue = self._sender_queue
        else:
            raise RuntimeError('uknown receiver: %s ' % caller_name)
        if queue.empty():
            return None
        else:
            logging.debug(' %s received message' % caller_name)
            return queue.get()

    def send(self, message):
        caller_name = self._get_caller_name()
        if caller_name == "<class 'simulator.sender.Sender'>":
            return self._receiver_queue.put(message)
        elif caller_name == "<class 'simulator.receiver.Receiver'>":
            return self._sender_queue.put(message)
            logging.debug(' %s sent message' % caller_name)
        else:
            raise RuntimeError('uknown receiver: %s ' % caller_name)

    def generate_channel_noise_model(self):
        channel_model(self._channel_quality_vector, self._max_time)
 
    def plot_channel(self):
        print(self._channel_quality_vector)
        visualizerEngine.PlotXYgraph(
            title = "generated channel", 
            vector = self._channel_quality_vector)
        
    def set_channel_to_fixed_quality_value(self, channel_quality):
        self._channel_quality_vector = numpy.full(self._max_time, channel_quality)
        
    def mark_message_as_garbage(self, size):
        max_size = 1000
        channel_quality = self._channel_quality_vector[self._time]
        probability_successful_transmission = 100 - (((size/10) - ((channel_quality*size)/max_size)))
        logging.debug('Probability of successful transmission %d' % probability_successful_transmission)
        if random.uniform(0, 100) < probability_successful_transmission:
            return False
        else:
            return True

    def get_current_cqi(self):
        if self._csvfile != None:
            self._csvfile.write("{}\n".format(self._channel_quality_vector[self._time]))
        return self._channel_quality_vector[self._time]
        
    def get_simulation_length(self):
        return self._max_time

    def reset_time(self):
        self._time = 0

    def initialize_seed_for_channel_model(self, seed = 0):
        self._seed = seed
        random.seed(seed)
        
    def register_observer(self, observer):
        self._observer_list.add(observer)

    def register_instance_to_monitor_time(self, instance):
        self._instances_monitoring_time_list.add(instance)

    def increment_time_base(self):
        self._time += 1
        for instance in self._instances_monitoring_time_list:
            instance.increment_time()

    def get_time(self):
        return self._time


def channel_model(channel_vector, max_time):
    initial_CQ = 50
    current_CQ = initial_CQ
    time_index = 0
    channel_vector[time_index] = current_CQ
    time_index += 1
    while 1:
        next_limit = int(random.uniform(0, 100))
        rate = (random.uniform(1, MAX_RATE_DOWN))
        if next_limit < current_CQ:
            while current_CQ > next_limit:
                current_CQ -= rate
                current_CQ = max(0, current_CQ)
                channel_vector[time_index] = current_CQ
                time_index += 1
                if time_index >= (max_time - 1):
                    return
        elif next_limit > current_CQ:
            rate =  (random.uniform(1, MAX_RATE_UP))
            while current_CQ < next_limit:
                current_CQ += rate
                current_CQ = min(100, current_CQ)
                channel_vector[time_index] = current_CQ
                time_index += 1
                if time_index >= (max_time - 1):
                    return
