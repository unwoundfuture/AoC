with open('input.txt') as sizes_txt:
	sizes = sizes_txt.read()
disk = []
for i in range(len(sizes)):
	if i % 2 == 0:
		disk += [i // 2 for _ in range(int(sizes[i]))]
	else:
		disk += ['.' for _ in range(int(sizes[i]))]

i = 0
for j in range(len(disk) - 1, -1, -1):
	while disk[i] != '.':
		i += 1
	if i > j: break
	disk[i], disk[j] = disk[j], '.'

s = 0
for i in range(len(disk)):
	if disk[i] == '.': break
	s += i * disk[i]
print(s)