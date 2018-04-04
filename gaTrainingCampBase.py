#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gaTrainingCampBase.py
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

import logging
import packetSizeEstimatorBase

DEFAULT_POPULATION_SIZE = 10
DEFAULT_MAX_GENERATIONS = 10

class gaTrainingCampBase(object):
    """A class for """

    def __init__(self):
        print("Trainning camp created!")
        self.max_generations = DEFAULT_MAX_GENERATIONS
        self.population_size = DEFAULT_POPULATION_SIZE
        self.population_list = []
        self.estimator = None

    def register_estimator(self, estimator):
        self.estimator = estimator

    def reset(self):
        pass

    def run(self):
        self.create_population()
        self.evolve_population()

    def evolve_population(self)
        while generations < self.max_generations:
            self.evaluate_fitness()
            self.selection()
            self.crossover()
            self.mutation()
            generations += 1 

    def create_population(self):
        for n in range(self.population_size):
            self.population_list.add(self.estimator())
        
    def evaluate_fitness(self):
        self._sort_population_by_fitness()
        pass
        
    def selection(self):
        pass
        
    def crossover(self):
        pass

    def mutation(self):
        pass

    def _sort_population_by_fitness(self):
        pass

