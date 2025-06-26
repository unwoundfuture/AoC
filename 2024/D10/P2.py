from functools import lru_cache

with open('input.txt') as f:
	trails = [[int(c) for c in l.strip()] for l in f]
mx, my = len(trails) - 1, len(trails[0]) - 1

@lru_cache(maxsize=(mx + 1) * (my + 1))
def score(x, y):
	s, n = 0, trails[x][y] + 1
	if n == 10: return 1
	if x != 0 and trails[x - 1][y] == n:
		s += score(x - 1, y)
	if x != mx and trails[x + 1][y] == n:
		s += score(x + 1, y)
	if y != 0 and trails[x][y - 1] == n:
		s += score(x, y - 1)
	if y != my and trails[x][y + 1] == n:
		s += score(x, y + 1)
	return s

trailheads, t = ((i, j) for i in range(mx + 1) for j in range(my + 1) if trails[i][j] == 0), 0
for head in trailheads: t += score(*head)
print(t)