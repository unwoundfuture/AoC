with open('input.txt') as lists_txt:
	lists = lists_txt.readlines()
l1, l2 = [], []
for items in lists:
	items = items.split()
	l1.append(int(items[0]))
	l2.append(int(items[1]))
l1.sort()
l2.sort()

s = 0
for i in range(len(l1)):
	s += abs(l1[i] - l2[i])
print(s)