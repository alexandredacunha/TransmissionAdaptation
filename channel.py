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
import Queue
import inspect
import random
import numpy
import messages
import logging

class Channel(object):
    """A class for """
    
    def __init__(self, simulation_length):
        self._receiver_queue = Queue.Queue()
        self._sender_queue = Queue.Queue()
        self._max_time = simulation_length
        self._comunication_quality_vector = numpy.full(self._max_time, 300)
        self._time = 0

    def _get_caller_name(self):
        stack = inspect.stack()
        the_class = stack[2][0].f_locals["self"].__class__
        return str(the_class)
    
    def receive(self):
        caller_name = self._get_caller_name()
        if caller_name == "<class 'receiver.Receiver'>":
            queue = self._receiver_queue
        elif caller_name == "<class 'sender.Sender'>":
            queue = self._sender_queue
        else:
            raise RuntimeError('uknown sender')
        if queue.empty():
            return None
        else:
            logging.debug(' %s received message' % caller_name)
            return queue.get()

    def send(self, message):
        caller_name = self._get_caller_name()
        if caller_name == "<class 'sender.Sender'>":
            return self._receiver_queue.put(message)
        elif caller_name == "<class 'receiver.Receiver'>":
            return self._sender_queue.put(message)
            logging.debug(' %s sent message' % caller_name)
        else:
            raise RuntimeError('uknown receiver')

    def generate_channel_noise_model(self):
        pass
        
    def set_channel_to_fixed_quality_value(self, channel_quality):
        self._comunication_quality_vector = numpy.full(self._max_time, channel_quality)
        
    def mark_message_as_garbage(self, size):
        max_size = 1000
        channel_quality = self._comunication_quality_vector[self._time]/10
        probability_failing_transmission = 100 - ((size/10) - ((channel_quality*size)/max_size))
        logging.debug('Probability of failing transmission %d' % probability_failing_transmission)
        if random.uniform(0, 100) < probability_failing_transmission:
            return False
        else:
            return True

    def increment_time_base(self):
        self._time += 1

    def get_time(self):
        return self._time
