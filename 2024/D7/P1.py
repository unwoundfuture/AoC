with open('input.txt') as equations_file:
	equations = equations_file.readlines()

operators_n, t = {0: ['+', '*']}, 0
for equation in equations:	
	equation.strip('\n')
	result, values = equation.split(':')
	result = int(result)
	values = [int(value) for value in values.split()]
	n = len(values) - 1
	operators = operators_n.get(n)
	if not operators:
		operators = ['+', '*']
		while len(operators[0]) < n:
			new_operators = []
			for operator in operators:
				new_operators.append(operator + '+')
				new_operators.append(operator + '*')
			operators = new_operators
		operators_n[n] = operators
	for i in range(len(operators)):
		s = values[0]
		for j in range(len(operators[i])):
			if operators[i][j] == '+': s += values[j + 1]
			else: s *= values[j + 1]
		if s == result:
			t += result
			break
	print(t)