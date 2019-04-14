#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simulationMain.py
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

from simulator import receiver
from simulator import sender
from simulator import channel
import visualizerEngine
from packetsizecalculator import packetSizeEstimator

import os
import sys
import time
import argparse
import logging
import csv
from copy import copy

results=[]
row=[]
    

def parse_arguments():
    """Provide a command line interface and parse provided arguments."""
    parser = argparse.ArgumentParser(description='AI experiment')
#    parser.add_argument('-d', help="Directory where to store the log", dest="log_dir", required=False)
#    parser.add_argument('-l', help="Log file name", dest="log_name", required=False
#    parser.add_argument('-s', help="Log size limit", dest='file_limit', type=int, default=0)
    return parser.parse_args()

def setup_and_run_simulation(simulation_length, data_size, channel_quality):

    #Channel setup
    interface = channel.Channel(simulation_length)
    #interface.generate_channel_noise_model()
    #interface.plot_channel()
    #exit()
    interface.set_channel_to_fixed_quality_value(channel_quality)
    
    #Packet size Estimator configuration
    packet_estimator = packetSizeEstimator.FixedPacketSize()
    packet_estimator.packet_size = data_size
    
    #Receiver config
    my_receiver = receiver.Receiver()
    my_receiver.register_interface(interface)
    
    #sender config
    my_data_generator = sender.Sender()
    my_data_generator.register_packet_size_estimator(packet_estimator)
    my_data_generator.register_interface(interface)
    
    print("packet size: " + str(data_size))
    print("channel quality: " + str(channel_quality))

    while interface.get_time() < simulation_length:
        my_data_generator.run()
        my_receiver.run()
        interface.increment_time_base()
        
    my_receiver.print_stats()
    row.append(my_receiver.stats.total_data_received)

def write_to_csv():
    output_file = open("csvfile.csv", "w")
    writer = csv.writer(output_file)
    writer.writerows(results)

def show_channel_model(args):
    """Start the syslog service.

    :param args: Information provided by the user as argparse arguments.
    """
    simulation_length = 1000
    
    #logging.basicConfig(filename='mainlog.log',level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    for payload_size in range(0, 1050, 50):
        for channel_quality in range(0, 110, 10):
            setup_and_run_simulation(simulation_length, payload_size, channel_quality)
        print(row)
        new_row = copy(row)
        results.append(new_row)
        del row[:]
    
    write_to_csv()
    t = visualizerEngine.CsvPlot3D(csvfile = 'csvfile.csv', title = 'Throughput(channel_quality, packet_size)')

def main():
    """Logic of the script."""
    args = parse_arguments()
    show_channel_model(args)
    sys.stdout.flush()
    #loop()

if __name__ == '__main__':
    main()
