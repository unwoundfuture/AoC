with open('input.txt') as grid_txt:
	grid = [row.strip('\n') for row in grid_txt.readlines()]
maxx, maxy = len(grid[0]) - 1, len(grid) - 1
for i in range(maxy + 1):
	grid[i] = [k for k in grid[i]]
	for j in range(maxx + 1):
		if grid[i][j] == '^':
			x, y, direction, grid[i][j] = j, i, 'up', 'X'
			break

s = 1
while True:
	if grid[y][x] != 'X':
		s += 1
		grid[y][x] = 'X'
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
print(s)