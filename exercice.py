#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools

#Générez la liste des maximums d'une liste de listes de nombres. On veut donc le maximum de chacune des listes.
def get_maximums(numbers):
	return [max(element) for element in numbers]

def join_integers(numbers):
	return int("".join([str(element) for element in numbers]))

def generate_prime_numbers(limit):
	return [0]

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [""]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
