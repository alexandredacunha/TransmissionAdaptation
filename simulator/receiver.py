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
from simulator import messages

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
        


class Receiver(object):
    """A class for """

    def __init__(self):
        self.interface = None
        self.total_data = 0
        self.stats = ReceiverStatistics()
        print("receiver created!")

    def register_interface(self, interface):
        self.interface = interface
        
    def receive(self):
        return self.interface.receive()
        
    def send(self, msg):
        return self.interface.send(msg)
        
    def _handle_payload_msg(self, msg):
        response = messages.AckNackMsg()
        if msg.discard == True:
            response.acknack = "NACK"
            self.stats.total_nacks += 1
        else:
            response.acknack = "ACK"
            self.total_data += msg.payload_size
            self.stats.total_data_received += msg.payload_size
            self.stats.total_acks += 1
        self.send(response)
    
    def print_stats(self):
        self.stats.print_all_stats()
            
    def run(self):
        msg = self.receive()
        if msg != None:
            if msg.msg_id == 1:
                self._handle_payload_msg(msg)
