import re

with open('input.txt') as words_txt:
	words = [word.strip() for word in words_txt.readlines()]

s = 0
pair = re.compile(r'([a-z][a-z]).*(\1)')
letter = re.compile(r'([a-z]).(\1)')
for word in words:
	if pair.search(word) and letter.search(word): s += 1
print(s)