with open('input.txt') as grid_file:
	grid = [row.strip('\n') for row in grid_file.readlines()]

s = 0
for i in range(len(grid) - 2):
	for j in range(len(grid[0]) - 2):
		x, y, z = grid[i][j] + grid[i][j+2], grid[i+1][j+1], grid[i+2][j] + grid[i+2][j+2]
		if y == 'A' and ((x == 'MM' and z == 'SS') or (x == z == 'MS') or (x == z == 'SM') or (x == 'SS' and z == 'MM')): s += 1
print(s)