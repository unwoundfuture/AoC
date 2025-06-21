with open('input.txt') as moves_txt:
	moves = moves_txt.read()

visited_houses, x, y, xr, yr, turn, s = [(0, 0)], 0, 0, 0, 0, 1, 1
for move in moves:
	if move == '^':
		if turn == 1: y += 1
		else: yr += 1
	elif move == '>':
		if turn == 1: x += 1
		else: xr += 1
	elif move == 'v':
		if turn == 1: y -= 1
		else: yr -= 1
	else:
		if turn == 1: x -= 1
		else: xr -= 1
	if turn == 1:
		if (x, y) not in visited_houses:
			s += 1
			visited_houses.append((x, y))
	else:
		if (xr, yr) not in visited_houses:
			s += 1
			visited_houses.append((xr, yr))
	turn *= -1
print(s)