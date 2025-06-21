with open('input.txt') as strings_txt:
	strings = [s.strip() for s in strings_txt.readlines()]

t = 0
for s in strings:
	t += 4
	i = 1
	while i < len(s) - 1:
		if s [i] == '"' or s[i] == '\\': t += 1
		i += 1
print(t)