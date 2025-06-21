with open('input.txt') as grid_file:
	grid = grid_file.readlines()

s = 0
for i in range(len(grid)): #Check horizontally.
	if grid[i][-1] == '\n': grid[i] = grid[i][:-1]
	for j in range(len(grid[i]) - 3):
		if grid[i][j:j+4] == 'XMAS' or grid[i][j:j+4] == 'SAMX': s += 1
for i in range(len(grid) - 3): #Check vertically.
	for j in range(len(grid[0])):
		x = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
		if x == 'XMAS' or x == 'SAMX': s += 1
for i in range(len(grid) - 3): #Check both diagonals.
	for j in range(len(grid[0]) - 3):
		x = grid[i][j] + grid[i+1][j +1] + grid[i+2][j+2] + grid[i+3][j+3]
		if x == 'XMAS' or x == 'SAMX': s += 1
		y = grid[i+3][j] + grid[i+2][j +1] + grid[i+1][j+2] + grid[i][j+3]
		if y == 'XMAS' or y == 'SAMX': s += 1
print(s)