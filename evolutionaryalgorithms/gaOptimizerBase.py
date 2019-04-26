#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gaOptimizerBase.py
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
import random
import gc

class gaOptimizerBase(object):
    """A class for """

    def __init__(self, population_size = 10, generations = 10, winners_pct = 40.0, crossover_prob = 0.5, mutation_prob = 0.1):
        print("Trainning camp created!")
        self.max_generations = generations
        self.population_size = population_size
        self.population_list = []
        self._winners_list = []
        self._new_idividuals_created_from_genetic_operations_list = []
        self.estimator = None
        self.number_of_winners = self.population_size/2
        self.crossover_probability = crossover_prob
        self.mutation_probability = mutation_prob
        self._winners_pct = winners_pct 
        self._nbr_of_winners = int(self._winners_pct * self.population_size)

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
            gc.collect()

    def create_population(self):
        for n in range(self.population_size):
            self.population_list.add(self.estimator())

    def _evaluate_fitness(self):
        self._sort_population_by_fitness()
        pass

    def selection(self):
        self._discard_weakest_specimens()

    def crossover(self):
        self._create_offsprings_as_crossover_from_top_winners()
        self._create_offsprings_as_crossover_from_random_winners()

    def mutation(self):
        self._apply_random_mutations_on_each_offspring_to_add_some_variations()
        self._merge_lists_to_create_new_population_ready_for_next_round()
        
    def _merge_lists_to_create_new_population_ready_for_next_round(self):
        self.population_list = self._winners_list + self._new_idividuals_created_from_genetic_operations_list

    def _sort_population_by_fitness(self):
        self.population_list.sort(key=lambda x: x.score, reverse = True)

    def _discard_weakest_specimens(self):
        nbr_of_specimens_to_discard = self.population_size - self._nbr_of_winners
        self._winners_list = self.population_list[:-nbr_of_specimens_to_discard]

# below this point should be implemented in derived classes for other genetic algorithms implementations

    def _create_offsprings_as_crossover_from_top_winners(self)
        pass

    def _create_offsprings_as_crossover_from_random_winners(self)
        pass

    def _apply_random_mutations_on_each_offspring_to_add_some_variations(self):
        pass
