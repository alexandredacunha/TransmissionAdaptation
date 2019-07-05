#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VisualizerEngine.py
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

"""
This creates a 3D mesh with perlin noise to simulate
a terrain. The mesh is animated by shifting the noise
to give a "fly-over" effect.
If you don't have pyOpenGL or opensimplex, then:
    - conda install -c anaconda pyopengl
    - pip install opensimplex
"""

import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LightSource
from matplotlib import cm
import pandas as pd
from numpy import genfromtxt
import numpy as np
from scipy.ndimage.interpolation import shift


class XYgraph_live():
    def __init__(self, title = 'not given', x_span = 100):
        self._num_charts = 0
        self._x_span = x_span
        self._ylabels = []
        self._data_series_vector = None
        self._time_base = 0
        self._graph = PlotXYgraph()

    def add(self, label):
        '''
        Adds new plot to the set.
        '''
        self._ylabels.add(label)
        new_vector = np.zeros(x_span)
        self._data_series_vector = np.stack(self._data_series_vector,
                                            new_vector)

    def update_value(self, label, value):
        #get index of label 
        #with index put value in the end of the correct vector
        pass

    def animate(self):
        animation.FuncAnimation(self._graph.plot(title = 'not given', 
                                vector = self_.vector_list, 
                                ylabels_vector = None, 
                                dataseries = "rows")

    def shift_vectors_left(self, shift):
        shift(self_.vector_list[0], shift, cval=np.NaN)
        pass

    def increment_time(self, increment = 1):
        self._time_base += increment
        self.shift_vectors_left(shift = increment)


class PlotXYgraph_from_multiple_csvfiles():
    def __init__(self, title = 'not given', csvfile_list = None):
        """
        plot xy chart using matplotlib
        """
        pass

    def show(self):
        pass


class PlotXYgraph():
    def __init__(self):
        pass

    def plot(self, title = 'not given', vector = None, csvfile = None, ylabels_vector = None, dataseries = "columns"):
        """
        plot xy chart using matplotlib
        """
        if csvfile != None:
            chart_data = genfromtxt(csvfile, delimiter=',')
            if title == "not given":
                title = os.path.basename(csvfile)
        else:
            chart_data = vector
        self.fig = plt.figure(title)
        try:
            len(chart_data[0])
            chart_data = np.array(chart_data)
            if dataseries == "columns":
                chart_data = chart_data.T
            num_charts = len(chart_data)
        except TypeError:
            num_charts = 1
        if ylabels_vector != None:
            data_label = ylabels_vector
        else:
            data_label = ["dummy"] * num_charts
        chart_num = 1
        for data_series_vector in chart_data:
            if num_charts == 1:
                data_series_vector = chart_data
            ax = self.fig.add_subplot(num_charts, 1, chart_num ,ylabel = data_label[chart_num-1])
            ax.plot(data_series_vector)
            ax.set_yticklabels([])
            #ax.set_xlim(left=0, right=DAY_SIZE)
            if chart_num < num_charts:
                ax.set_xticklabels([])
            chart_num = chart_num + 1
            ax.yaxis.label.set_fontsize(7)
            ax.yaxis.label.set_rotation(0)
            if num_charts == 1:
                break
        plt.ylim(bottom=0)
        plt.show()

    def show(self):
        pass


class CsvPlot3D():
    def __init__(self, title = 'not given', csvfile = 'default.csv'):
        """
        plot 3D chart using matplotlib
        """
        self.title = title
        # setup the view window
 
        my_data = genfromtxt(csvfile, delimiter=',')

        x = np.arange(0, 100, 100/len(my_data[0]))
        y = np.arange(0, 1000, 1000/len(my_data))
         
        # Make the plot 3d
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x, y = np.meshgrid(x, y)
        ls = LightSource(270, 45)
        # To use a custom hillshading mode, override the built-in shading and pass
        # in the rgb colors of the shaded surface calculated from "shade".
        rgb = ls.shade(my_data, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
        ax.plot_surface(x, y, my_data, rstride=1, cstride=1, facecolors=rgb, linewidth=0, antialiased=False, shade=False)

        cset = ax.contourf(x, y, my_data, zdir='z', offset=0, cmap=cm.gist_yarg)
        #cset = ax.contourf(x, y, my_data, zdir='x', offset=-10, cmap=cm.coolwarm)
        #cset = ax.contourf(x, y, my_data, zdir='y', offset=-10, cmap=cm.coolwarm)

        #ax.scatter(df['Y'], df['X'], df['Z'])
        #ax.set_xlim(0, 19)
        #ax.set_ylim(0, 10)
        ax.set_xlabel('channel quality')
        ax.set_ylabel('packet size')
        ax.set_zlabel('Throughput')

        plt.show()


if __name__ == '__main__':
    #t = CsvPlot3D(csvfile = 'csvfile.csv')
    #test live graphic
    chart = XYgraph_live()
    chart.add("test_data")
    
