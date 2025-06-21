with open('input.txt') as strings_txt:
	strings = [string.strip() for string in strings_txt.readlines()]

t = 0
for s in strings:
	t += 2
	i = 1
	while i < len(s) - 2:
		if s[i:i+2] == '\\"' or s[i:i+2] == '\\\\':
			t += 1
			i += 2
		elif s[i:i+2] == '\\x':
			t += 3
			i += 4
		else: i += 1
print(t)