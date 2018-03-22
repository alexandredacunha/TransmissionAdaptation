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


class PacketSizeEstimatorBase(object):
    """Base class for packet size estimator"""
    def __init__(self):
        self.channel_quality_reported = None
        #ack = 1; nack = 0
        self.transmission_results = None

    def get_optimal_size_for_next_transmission(self):
        return self._run_algorithm()
        
    def store_last_transmission_result(self):
        pass
    
    def _run_algorithm(self):
        pass


class FixedPacketSize(PacketSizeEstimatorBase):
    """fixed packet size estimator"""
    def __init__(self):
        default_size = 1000
        self.packet_size = default_size

    def get_optimal_size_for_next_transmission(self):
        return self.packet_size
  

