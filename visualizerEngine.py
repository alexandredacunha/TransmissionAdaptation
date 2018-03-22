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

import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph
import sys
from opensimplex import OpenSimplex

class PlotXYgraph(object):
    def __init__(self, title = 'not given', vector = None):
        """
        Initialize the graphics window and mesh
        """
        self.title = title
        self.app = QtGui.QApplication(sys.argv)
        
        self.win = pyqtgraph.GraphicsWindow(title=title)
        self.win.resize(500,200)
        self.win.setWindowTitle(title)
        p1 = self.win.addPlot(title=title, y=vector)
        self.start()
        
    def start(self):
        """
        get the graphics window open and setup
        """
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

class CsvPlot3D(object):
    def __init__(self, title = 'not given', csvfile = 'default.csv'):
        """
        Initialize the graphics window and mesh
        """
        self.title = title
        # setup the view window
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.setGeometry(100, 100, 500, 500)
        self.w.show()
        self.w.setWindowTitle(self.title)
        self.w.setCameraPosition(distance=25)
        
        #load data from CSV
        z = np.loadtxt(open(csvfile, "rb"), delimiter=",", skiprows=0)
        x_length = z.shape[0]
        y_length = z.shape[1]
        
        #add grid
        g = gl.GLGridItem()
        g.scale(1,float(y_length)/float(x_length),1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        self.w.addItem(g)
        
        p1 = gl.GLSurfacePlotItem(
                z=(z/float(z.max())), 
                shader='shaded', 
                color=(0.5, 0.5, 1, 0),
                drawEdges=True,
                drawFaces=True,
                smooth=True 
        )
        #print np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
        #print (z/float(z.max()))
        p1.scale(1.0, 1.0, 10)
        p1.translate(-x_length/2, -y_length /2, 0)
        self.w.addItem(p1)
        
        self.start()


    def start(self):
        """
        get the graphics window open and setup
        """
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def animation(self):
        """
        calls the update method to run in a loop
        """
        #timer = QtCore.QTimer()
        #timer.timeout.connect(self.update)
        #timer.start(10)
        self.start()
        #self.update()


if __name__ == '__main__':
    t = CsvPlot3D(csvfile = 'csvfile.csv')


