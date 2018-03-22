#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nnPacketSizeEstimatorTensorFlow.py
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

class NNPacketSizeEstimatorTensorFlow(PacketSizeEstimatorBase):
    def __init__(self):
        default_size = 1000
        self.packet_size = default_size
        
    def multilayer_perceptron(self, x, weights, biases, keep_prob):
        layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
        layer_1 = tf.nn.relu(layer_1)
        layer_1 = tf.nn.dropout(layer_1, keep_prob)
        out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
        return out_layer
    
    def create    
        n_hidden_1 = 38
        n_input = train_x.shape[1]
        n_classes = train_y.shape[1]

        weights = {
            'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
            'out': tf.Variable(tf.random_normal([n_hidden_1, n_classes]))
        }

        biases = {
            'b1': tf.Variable(tf.random_normal([n_hidden_1])),
            'out': tf.Variable(tf.random_normal([n_classes]))
        }



def main():
	
	return 0

if __name__ == '__main__':
	main()

