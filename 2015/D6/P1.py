import re

with open('input.txt') as instructs_txt:
	instructs = [i.strip() for i in instructs_txt.readlines()]

regex = re.compile(r'(turn on|toggle|turn off) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})')
grid = [[False] * 1000 for _ in range(1000)]

for instruct in instructs:
	command, a, b, x, y = regex.match(instruct).groups()
	if command == 'turn on':
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1): grid[i][j] = True
	elif command == 'turn off':
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1): grid[i][j] = False
	else:
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1): grid[i][j] = not grid[i][j]

s = 0
for row in grid:
	for cell in row:
		if cell: s += 1
print(s)