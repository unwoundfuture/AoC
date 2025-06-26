with open('input.txt') as f:
	trails = [[int(c) for c in l.strip()] for l in f]
mx, my = len(trails) - 1, len(trails[0]) - 1

def score(x, y, reached=None):
	if reached is None: reached = set()
	s, n = 0, trails[x][y] + 1
	if n == 10 and (x, y) not in reached:
		reached.add((x, y))
		return 1
	if x != 0 and trails[x - 1][y] == n:
		s += score(x - 1, y, reached)
	if x != mx and trails[x + 1][y] == n:
		s += score(x + 1, y, reached)
	if y != 0 and trails[x][y - 1] == n:
		s += score(x, y - 1, reached)
	if y != my and trails[x][y + 1] == n:
		s += score(x, y + 1, reached)
	return s

trailheads, t = ((i, j) for i in range(mx + 1) for j in range(my + 1) if trails[i][j] == 0), 0
for head in trailheads: t += score(*head)
print(t)