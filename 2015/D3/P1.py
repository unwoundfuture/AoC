with open('input.txt') as moves_txt:
	moves = moves_txt.read()

visited_houses, x, y, s = [(0, 0)], 0, 0, 1
for move in moves:
	if move == '^': y += 1
	elif move == '>': x += 1
	elif move == 'v': y -= 1
	else: x -= 1
	if (x, y) not in visited_houses:
		s += 1
		visited_houses.append((x, y))
print(s)