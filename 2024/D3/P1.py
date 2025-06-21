import re

with open('input.txt') as memory_file:
	memory = memory_file.read()

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
s = 0
for multiplication in regex.findall(memory):
	s += int(multiplication[0]) * int(multiplication[1])
print(s)