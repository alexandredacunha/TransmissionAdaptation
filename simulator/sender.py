#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sender.py
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

from simulator import messages
import logging

class Sender():
    """A class for """

    def __init__(self):
        self.interface = None
        self.packet_size_estimator = None
        print("sender created!")

    def register_packet_size_estimator(self, packet_size_estimator):
        self.packet_size_estimator = packet_size_estimator

    def register_interface(self, interface):
        self.interface = interface
        
    def receive(self):
        return self.interface.receive()
        
    def send(self, msg):
        return self.interface.send(msg)
        
    def _handle_acknack(self, acknack_msg):
        #print "Got " + msg.acknack
        self.packet_size_estimator.store_last_tx_result(acknack_msg.acknack, acknack_msg.cqi)
        pass

    def _build_data_packet(self):
        data_msg = messages.DataPacketMsg()
        data_msg.payload_size = self.packet_size_estimator.get_optimal_size_for_next_tx()
        data_msg.discard = self.interface.mark_message_as_garbage(data_msg.payload_size)
        return data_msg

    def run(self):
        msg = self.receive()
        if msg != None:
            if msg.msg_id == 2:
                self._handle_acknack(msg)
        data_msg = self._build_data_packet()
        data_msg.cqi = self.interface.get_current_cqi()
        self.send(data_msg)
