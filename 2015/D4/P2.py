from hashlib import md5

with open('input.txt') as key_txt:
	key = key_txt.read()

i = 1
while True:
	test = key + str(i)
	h = md5(test.encode())
	hex_md5 = h.hexdigest()
	if hex_md5[:6] == '000000':
		break
	i += 1
print(i)