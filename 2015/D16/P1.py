with open('input.txt') as f:
	data = [l.strip().split() for l in f.readlines()]

sues = [{d[i][:-1]: int(d[i+1].strip(',')) for i in range(2, len(d), 2)} for d in data]
print(sues)

criteria = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for i, sue in enumerate(sues):
	found = True
	for attribute in sue:
		if sue[attribute] != criteria[attribute]:
			found = False
			break
	if found: break
print(i + 1)