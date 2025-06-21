with open('/storage/emulated/0/python_projects/advent/2015/1_input.txt') as instructions_txt:
	instructions = instructions_txt.read()

position = 0
for i in range(len(instructions)):
	if instructions[i] == '(': position += 1
	else: position -= 1
	if position == -1:
		print(i + 1)
		break