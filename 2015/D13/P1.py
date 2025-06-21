from collections import defaultdict
from itertools import permutations

with open('input.txt') as rules_txt:
	rules = [rule.strip().split() for rule in rules_txt.readlines()]

happiness_rules = defaultdict(dict)
for rule in rules:
	happiness_rules[rule[0]][rule[-1][:-1]] = int(rule[3]) if rule[2] == 'gain' else -int(rule[3])


max_happiness = 0
for perm in permutations(happiness_rules.keys()):
	happiness = 0
	for i in range(len(perm)):
		left = happiness_rules[perm[i]][perm[i-1]]
		right = happiness_rules[perm[i]][perm[(i+1)%len(perm)]]
		happiness += left + right
	if happiness > max_happiness: max_happiness = happiness
print(max_happiness)