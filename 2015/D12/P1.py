import re

with open('input.txt') as data_json:
	data = data_json.read()

pattern, total = re.compile(r'-?\d+'), 0
for n in pattern.findall(data):
	total += int(n)
print(total)