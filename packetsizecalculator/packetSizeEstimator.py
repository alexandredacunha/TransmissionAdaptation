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

DEFAULT_SIZE = 1000
MAX_SIZE = 1000
MIN_SIZE = 0

class PacketSizeEstimatorBase():
    """Base class for packet size estimator"""
    def __init__(self):
        self.channel_quality_reported = None
        #ack = 1; nack = 0
        self.transmission_results = None
        self.score = 0

    def get_optimal_size_for_next_tx(self):
        return self._run_algorithm()
        
    def store_last_tx_result(self, acknack, cqi):
        pass
    
    def _run_algorithm(self):
        pass


class FixedPacketSize(PacketSizeEstimatorBase):
    """fixed packet size estimator"""
    def __init__(self):
        self.packet_size = DEFAULT_SIZE

    def get_optimal_size_for_next_tx(self):
        return self.packet_size


class SimpleEstimator(PacketSizeEstimatorBase):
    """simple packet size estimator"""
    def __init__(self):
        self.packet_size = DEFAULT_SIZE/2
        self._up_rate = 1
        self._down_rate = 1

    def get_optimal_size_for_next_tx(self):
        return self.packet_size

    def store_last_tx_result(self, acknack, cqi):
        if acknack == "ACK":
            self.packet_size = min(self.packet_size + self._up_rate, 1000)
        if acknack == "NACK":
            self.packet_size = max(self.packet_size - self._down_rate, 0)

