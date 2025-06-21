with open('input.txt') as f:
	lines = [line.strip().split() for line in f.readlines()]

properties = [(int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10][-1])) for line in lines]

high_score = 0
for i in range(101):
	for j in range(101 - i):
		for k in range(101 - (i + j)):
			l = 100 - (i + j + k)
			score = 1
			for p in range(4):
				score *= (i * properties[0][p] + j * properties[1][p] + k * properties[2][p] + l * properties[3][p])
				if score < 0: break
			high_score = max(score, high_score)
print(high_score)