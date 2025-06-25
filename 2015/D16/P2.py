with open('input.txt') as f:
	data = [l.strip().split() for l in f.readlines()]

sues = [{d[i][:-1]: int(d[i+1].strip(',')) for i in range(2, len(d), 2)} for d in data]
c = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for i, sue in enumerate(sues):
	found = True
	for k, v in sue.items():
		if k in ('cats', 'trees'):
			if v <= c[k]:
				found = False
				break
		elif k in ('pomeranians', 'goldfish'):
			if v >= c[k]:
				found = False
				break
		elif v != c[k]:
			found = False
			break
	if found: break
print(i + 1)