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

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
from numpy import genfromtxt
import numpy as np
from matplotlib.colors import LightSource
from matplotlib import cm

class PlotXYgraph():
    def __init__(self, title = 'not given', vector = None):
        """
        plot xy chart using matplotlib
        """
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
    t = CsvPlot3D(csvfile = 'csvfile.csv')


