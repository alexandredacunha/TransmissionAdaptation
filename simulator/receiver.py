#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  receiver.py
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

import logging
import statistics
from simulator import messages
from collections import deque

avgWindow = 10

class ReceiverStatistics():
    def __init__(self):
        self.total_data_received = 0
        self.total_acks = 0
        self.total_nacks = 0
        self.sizes = {}

    def print_all_stats(self):
        print("got " + str(self.total_data_received) + " data units")
        print("nr. Acks: " + str(self.total_acks))
        print("nr. Nacks: " + str(self.total_nacks))


class Receiver():
    """A class for """

    def __init__(self):
        self.interface = None
        self.total_data = 0
        self.stats = ReceiverStatistics()
        self._tp_calculation = deque(maxlen = avgWindow)
        self._observer_list = []
        print("receiver created!")

    def register_interface(self, interface):
        self.interface = interface
        
    def register_observer(self, observer):
        observer.add("receiver_throughput")
        observer.add("receiver_packet_size")
        observer.add("receiver_cqi")
        self.register_observer(observer)
        
    def receive(self):
        return self.interface.receive()
        
    def send(self, msg):
        return self.interface.send(msg)
        
    def _handle_payload_msg(self, msg):
        response = messages.AckNackMsg()
        if msg.discard == True:
            response.acknack = "NACK"
            self.stats.total_nacks += 1
            self._tp_calculation.append(0)
        else:
            response.acknack = "ACK"
            self.total_data += msg.payload_size
            self.stats.total_data_received += msg.payload_size
            self.stats.total_acks += 1
            self._observer_value_update("receiver_packet_size", 
                                         msg.payload_size)
            self._tp_calculation.append(msg.payload_size)
        response.cqi = self.interface.get_current_cqi()
        self._observer_value_update("receiver_throughput", 
                                    statistics.mean(self._tp_calculation))
        self._observer_value_update("receiver_cqi", 
                                    response.cqi)
        self.send(response)

    def print_stats(self):
        self.stats.print_all_stats()
        
    def _observer_value_update(self, label, value):
        for observer in self._observer_list:
            observer.update_value(label, value)

    def run(self):
        msg = self.receive()
        if msg != None:
            if msg.msg_id == 1:
                self._handle_payload_msg(msg)
