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

	r = range(len(matrix))
	t = tsp.tsp([(0,0), (0,1), (1,0), (1,1)])
	# Dictionary of distance
	dist = {(i, j): matrix[i][j] for i in r for j in r}
	print(dist)
	print(r)
	print(tsp.tsp(r, dist))
