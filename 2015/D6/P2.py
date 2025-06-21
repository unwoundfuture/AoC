import re

with open('input.txt') as instructs_txt:
	instructs = [i.strip() for i in instructs_txt.readlines()]

regex = re.compile(r'(turn on|toggle|turn off) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})')
grid = [[0] * 1000 for _ in range(1000)]

s = 0
for instruct in instructs:
	command, a, b, x, y = regex.match(instruct).groups()
	if command == 'turn on':
		s += (int(x) - int(a) + 1) * (int(y) - int(b) + 1)
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1): grid[i][j] += 1
	elif command == 'turn off':
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1):
				if grid[i][j]:
					grid[i][j] -= 1
					s -= 1
	else:
		s += (int(x) - int(a) + 1) * (int(y) - int(b) + 1) * 2
		for i in range(int(a), int(x) + 1):
			for j in range(int(b), int(y) + 1): grid[i][j] += 2
print(s)