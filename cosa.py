import sys
import copy
import os
import json
import tsp
from tsp import tsp

matrices = json.loads(open('matrixZarpes.json').read())
matrixComuna = matrices["adjacency"]
matrix = matrices["distances"]

if __name__ == '__main__':

	a=3
	b=a
	a=4
	print(a,b)