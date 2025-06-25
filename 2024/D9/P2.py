with open('input.txt') as sizes_txt:
	sizes = sizes_txt.read()
disk = []
for i in range(len(sizes)):
	if i % 2 == 0:
		disk.append((i // 2, int(sizes[i])))
	else:
		disk.append(('.', int(sizes[i])))

j = len(disk) - 1 if disk[-1][0] != '.' else len(disk) - 2
while j > 0:
	n, l = disk[j]
	i = 1
	for i in range(j + 1):
		if disk[i][0] == '.' and disk[i][1] >= l: break
	if i < j:
		l2 = disk[i][1]
		disk[j] = ('.', l)
		disk[i] = (n, l)
		if l != l2: disk.insert(i + 1, ('.', l2 - l))
	while (disk[j][0] == '.' or disk[j][0] >= n) and j > 0:
		j -= 1

s, j = 0, 0
for i in range(len(disk)):
	if disk[i][0] != '.':
		n, l = disk[i]
		for k in range(j, j + l):
			s += k * n
		j += l
	else: j += disk[i][1]
print(s)