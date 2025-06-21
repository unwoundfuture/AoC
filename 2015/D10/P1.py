with open('input.txt') as numbers_txt:
	numbers = numbers_txt.read()

def look_and_say(n):
	if len(n) == 1: return '1' + n
	s, l = '', 1
	for i in range(1, len(n)):
		if n[i] == n[i-1]: l += 1
		else:
			s += str(l) + n[i-1]
			l = 1
	s += str(l) + n[-1]
	return s

for _ in range(40):
	numbers = look_and_say(numbers)
print(len(numbers))