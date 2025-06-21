from hashlib import md5

with open('input.txt') as key_txt:
	key = key_txt.read()

i = 1
while True:
	test = key + str(i)
	h = md5(test.encode())
	if h.hexdigest()[:5] == '00000':
		break
	i += 1
print(i)