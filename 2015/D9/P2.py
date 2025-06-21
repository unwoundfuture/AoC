from itertools import permutations
from collections import defaultdict

with open('input.txt') as input_txt:
	connections = [d.strip() for d in input_txt.readlines()]

distances = defaultdict(dict)
for connection in connections:
	x1, _, x2, _, d = connection.split()
	distances[x1][x2], distances[x2][x1] = int(d), int(d)

shortest_path, locations = 0, list(distances.keys())
for path in permutations(locations):
	path_distance = 0
	for i in range(len(path) - 1):
		path_distance += distances[path[i]][path[i+1]]
	if path_distance > shortest_path:
		shortest_path = path_distance
print(shortest_path)