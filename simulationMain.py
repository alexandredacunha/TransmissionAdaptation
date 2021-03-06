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

import os
import sys
import time
import argparse
import logging
import csv
import numpy as np
from copy import copy
from simulator import receiver
from simulator import sender
from simulator import channel
import visualizationtools.visualizerEngineMatplotlib as visualizerEngine
from packetsizecalculator import packetSizeEstimator
from packetsizecalculator import packetSizeEstimatorDQN
from packetsizecalculator import packetSizeEstimatorDQNFullRange

results=[]
row=[]

CSV_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), "csv_logs")

DEAFULT_SIMULATION_LENGTH = 1000

def parse_arguments():
    """Provide a command line interface and parse provided arguments."""
    parser = argparse.ArgumentParser(description='AI experiment')
#    parser.add_argument('-d', help="Directory where to store the log", dest="log_dir", required=False)
#    parser.add_argument('-l', help="Log file name", dest="log_name", required=False
#    parser.add_argument('-s', help="Log size limit", dest='file_limit', type=int, default=0)
    return parser.parse_args()

def setup_and_run_simulation(interface, packet_size_estimator, simulation_length):

    #Receiver config
    my_receiver = receiver.Receiver()
    my_receiver.register_interface(interface)
    
    #sender config
    my_data_generator = sender.Sender()
    my_data_generator.register_packet_size_estimator(packet_size_estimator)
    my_data_generator.register_interface(interface)

    while interface.get_time() < simulation_length:
        my_data_generator.run()
        my_receiver.run()
        interface.increment_time_base()
        
    my_receiver.print_stats()
    row.append(my_receiver.stats.total_data_received)

def write_to_csv():
    csv_filename_with_path = os.path.join(CSV_DIRECTORY, "csvfile.csv")
    output_file = open(csv_filename_with_path, "w")
    writer = csv.writer(output_file)
    writer.writerows(results)
    output_file.close()
    return csv_filename_with_path

def show_channel_model(args):
    """show_channel_model.

    :param args: Information provided by the user as argparse arguments.
    """
    simulation_length = 1000
    
    #logging.basicConfig(filename='mainlog.log',level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    for payload_size in range(0, 1050, 50):
        for channel_quality in range(0, 110, 10):
            print("packet size: " + str(payload_size))
            print("channel quality: " + str(channel_quality))
            #Channel setup
            interface = channel.Channel(simulation_length)
            interface.set_channel_to_fixed_quality_value(channel_quality)
            #Estimator setup
            estimator = packetSizeEstimator.FixedPacketSize()
            estimator.packet_size = payload_size
            #simulation start
            setup_and_run_simulation(interface, 
                                     estimator,
                                     simulation_length)
        print(row)
        new_row = copy(row)
        results.append(new_row)
        del row[:]

    csv_filename_with_path = write_to_csv()
    t = visualizerEngine.CsvPlot3D(csvfile = csv_filename_with_path, 
                                   title = 'Throughput(channel_quality, packet_size)')

def run_test(args, estimator, interface):
    """run_test_simple_estimator.

    :param args: Information provided by the user as argparse arguments.
    """
    simulation_length = interface.get_simulation_length()
    #logging.basicConfig(filename='mainlog.log',level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    setup_and_run_simulation(interface, 
                             estimator,
                             simulation_length)
    print(row)
    print(len(np.array(estimator.calculated_sizes)))
    reference_shape = ((interface._channel_quality_vector).shape)
     
    combined_chart_data = np.stack((interface._channel_quality_vector, 
                                    np.resize(np.array(estimator.calculated_sizes), reference_shape)))
    chart = visualizerEngine.PlotXYgraph()
    chart.plot(vector = combined_chart_data, 
                                 title = 'Estimator',
                                 dataseries = "rows")
    chart.show()

def main():
    """Logic of the script."""
    args = parse_arguments()
    if not os.path.exists(CSV_DIRECTORY):
        os.makedirs(CSV_DIRECTORY)

    #show_channel_model(args)

    simulation_length = DEAFULT_SIMULATION_LENGTH

    #Create channel
    interface = channel.Channel(simulation_length)
    interface.generate_channel_noise_model()

    interface.reset_time()
    interface.initialize_seed_for_channel_model()
    run_test(args, packetSizeEstimatorDQN.DQNEstimator_3_actions(), interface)

#    interface.reset_time()
#    interface.initialize_seed_for_channel_model()
#    run_test(args, packetSizeEstimatorDQNFullRange.DQNEstimatorFullRange(), interface)

#    interface.reset_time()
#    interface.initialize_seed_for_channel_model()
#    run_test(args, packetSizeEstimator.SimpleEstimator(), interface)
    
#    interface.reset_time()
#    interface.initialize_seed_for_channel_model()
#    run_test(args, packetSizeEstimator.OptimalEstimator(), interface)
    
    
    #t = visualizerEngine.CsvPlot3D(csvfile = 'csvfile.csv', title = 'Throughput(channel_quality, packet_size)')
    #t = visualizerEngine.PlotXYgraph(csvfile = 'csvfile.csv', title = 'Throughput(channel_quality, packet_size)')
    #t = visualizerEngine.PlotXYgraph(vector = [[1,2,3,4,5,6],[1,2,3,4,5,6]], title = 'Throughput(channel_quality, packet_size)', dataseries = "rows") 
    #t = visualizerEngine.PlotXYgraph(vector = [[1,2,3,4,5,6],[1,2,3,4,5,6]], title = 'Throughput(channel_quality, packet_size)', dataseries = "columns") 
    sys.stdout.flush()
    #loop()

if __name__ == '__main__':
    main()
