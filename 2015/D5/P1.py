import re

with open('input.txt') as words_txt:
	words = [word.strip() for word in words_txt.readlines()]

s = 0
vowels = re.compile('[aeiou]')
repeat = re.compile(r'([a-z])(\1)')
invalid = re.compile('ab|cd|pq|xy')
for word in words:
	v = len(vowels.findall(word))
	r = repeat.findall(word)
	i = invalid.findall(word)
	if v > 2 and r and not i: s += 1
print(s)