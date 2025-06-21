from copy import deepcopy
with open('input.txt') as grid_txt:
	grid = [row.strip('\n') for row in grid_txt.readlines()]
maxx, maxy = len(grid[0]) - 1, len(grid) - 1
for i in range(maxy + 1):
	grid[i] = [k for k in grid[i]]
	for j in range(maxx + 1):
		if grid[i][j] == '^':
			startx, starty, start_direction, grid[i][j] = j, i, 'up', 'Y'
			break

x, y, direction = startx, starty, start_direction
while True:
	if grid[y][x] == '.': grid[y][x] = 'X'
	if direction == 'up':
		if y == 0: break
		if grid[y - 1][x] == '#': direction = 'right'
		else: y -= 1
	elif direction == 'right':
		if x == maxx: break
		if grid[y][x + 1] == '#': direction = 'down'
		else: x += 1
	elif direction == 'down':
		if y == maxy: break
		if grid[y + 1][x] == '#': direction = 'left'
		else: y += 1
	elif direction == 'left':
		if x == 0: break
		if grid[y][x - 1] == '#': direction = 'up'
		else: x -= 1

def is_loop(g, start):
	previous = set()
	a, b, d = start
	while True:
		if (a, b, d) in previous: return True
		else: previous.add((a, b, d))
		if d == 'up':
			if b == 0: break
			if (g[b - 1][a] == '#'): d = 'right'
			else: b -= 1
		elif d == 'right':
			if a == maxx: break
			if g[b][a + 1] == '#': d = 'down'
			else: a += 1
		elif d == 'down':
			if b == maxy: break
			if g[b + 1][a] == '#': d = 'left'
			else: b += 1
		elif d == 'left':
			if a == 0: break
			if g[b][a - 1] == '#': d = 'up'
			else: a -= 1
	return False

path_positions = []
for i in range(maxy + 1):
	for j in range(maxx + 1):
		if grid[i][j] == 'X': path_positions.append((j, i))
s = 0
for position in path_positions:
	gridcopy = deepcopy(grid)
	gridcopy[position[1]][position[0]] = '#'
	if is_loop(gridcopy, (startx, starty, start_direction)): s += 1
print(s)