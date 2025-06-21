import re

with open('input.txt') as password_txt:
	password = password_txt.read()

def increment(p):
	carry, index = True, len(p) - 1
	while carry:
		order = ord(p[index]) + 1
		if order > 122:
			order -= 26
			carry = True
		else: carry = False
		p = p[:index] + chr(order) + p[index+1:]
		index -= 1
	return p

xxyy = re.compile(r'([a-z])(\1).*([^\1])(\3)')

while True:
	password = increment(password)
	iol, abc = False, False
	
	for char in password:
		if char in 'iol':
			iol = True
			break
	if iol: continue
	
	for i in range(len(password) - 2):
		if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
			abc = True
			break
	if not abc: continue
	
	if xxyy.search(password) is None: continue
	
	break
print(password)