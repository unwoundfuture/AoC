import re

with open('input.txt') as instructs_txt:
	instructs = [i.strip() for i in instructs_txt.readlines()]

ASSIGN = re.compile(r'(\d+|[a-z]+) -> ([a-z]+)')
NOT = re.compile(r'NOT ([a-z]+) -> ([a-z]+)')
OTHER = re.compile(r'([a-z]+|\d+) ([A-Z]+) ([a-z]+|\d+) -> ([a-z]+)')

signals = {}
while len(signals) < len(instructs):
	for i in range(len(instructs)):
		x = OTHER.match(instructs[i])
		if x:
			v1, op, v2, w = x.groups()
			v1 = int(v1) if v1.isdecimal() else signals.get(v1)
			v2 = int(v2) if v2.isdecimal() else signals.get(v2)
			if v1 != None and v2 != None:
				if op == 'AND': result = v1 & v2
				elif op == 'OR': result = v1 | v2
				elif op == 'LSHIFT': result = v1 << v2
				else: result = v1 >> v2
				signals[w] = result
		else:
			y = NOT.match(instructs[i])
			if y:
				v, w = y.groups()
				v = signals.get(v)
				if v != None:
					signals[w] = ~v
			else:
				z = ASSIGN.match(instructs[i])
				if z:
					v, w = z.groups()
					v = int(v) if v.isdecimal() else signals.get(v)
					if v != None:
						signals[w] = v
print(signals['a'])