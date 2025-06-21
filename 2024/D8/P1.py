with open('input.txt') as grid_txt:
	grid = [row.strip('\n') for row in grid_txt.readlines()]

maxx, maxy, indices = len(grid), len(grid[0]), {}
for i in range(maxx):
	for j in range(maxy):
		if grid[i][j].isalnum():
			indices.setdefault(grid[i][j], [])
			indices[grid[i][j]].append(complex(i, j))
			

covered_indices, s = set(), 0
for antenna, i in indices.items():
	for j in range(len(i) - 1):
		for k in range(j + 1, len(i)):
			v = i[k] - i[j]
			a1, a2 = i[j] - v, i[k] + v
			if (0 <= a1.real < maxx) and (0 <= a1.imag < maxy) and (a1 not in covered_indices):
				s += 1
				covered_indices.add(a1)
			if (0 <= a2.real < maxx) and (0 <= a2.imag < maxy) and (a2 not in covered_indices):
				s += 1
				covered_indices.add(a2)
print(s)