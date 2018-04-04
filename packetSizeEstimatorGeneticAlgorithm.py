#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  packetSizeEstimatorGeneticAlgorithm.py
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

import packetSizeEstimator

from keras.models import Sequential
from keras.layers import Dense
import numpy

class PacketSizeEstimatorGeneticAlgorithm(PacketSizeEstimatorBase):
    def __init__(self):
        default_size = 0
        self.packet_size = default_size
        self.model = None
        
    def create_model(self, )
        pass

def main():

    return 0

if __name__ == '__main__':
    main()

