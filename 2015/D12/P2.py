from collections import deque
import re

with open('input.txt') as data_json:
	data = data_json.read()

pattern, total = re.compile(r'-?\d+'), 0
for n in pattern.findall(data):
	total += int(n)
print(total)

obj_queue, unclosed, x = deque(), 0, None
for i in range(len(data)):
	if data[i] == '{':
		if x is None: x = i
		unclosed += 1
	elif data[i] == '}':
		unclosed -= 1
		if not unclosed:
			obj_queue.append((x+1, i))
			x = None
print(obj_queue)

while obj_queue:
	start, end = obj_queue.popleft()
	unclosed, children, x, red, red_child = 0, [], None, False, False
	for i in range(start, end):
		if data[i] == '{':
			if x is None: x = i
			unclosed += 1
		elif data[i] == '}':
			unclosed -= 1
			if not unclosed:
				if red_child:
					children.append((x+1, i))
					red_child = False
				x = None
		elif i < len(data) - 5 and data[i:i+6] == ':"red"':
			if unclosed:
				red_child = True
			else:
				red = True
				break
	
	if red:
		for n in pattern.findall(data[start:end]):
			total -= int(n)
	else:
		obj_queue.extend(children)
print(total)