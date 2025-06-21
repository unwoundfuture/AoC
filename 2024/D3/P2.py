import re

with open('input.txt') as memory_file:
	memory = memory_file.read()

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")
s, enabled = 0, True
for multiplication in regex.findall(memory):
	if multiplication[2] == 'do()': enabled = True
	elif multiplication[3] == "don't()": enabled = False
	elif enabled: s += int(multiplication[0]) * int(multiplication[1])
print(s)