with open('input.txt') as lists_txt:
	lists = lists_txt.readlines()
l1, l2 = [], []
for items in lists:
	items = items.split()
	l1.append(int(items[0]))
	l2.append(int(items[1]))

l1_counts, l2_counts = {}, {}
for item in l1:
	l1_counts.setdefault(item, 0)
	l1_counts[item] += 1
for item in l2:
	l2_counts.setdefault(item, 0)
	l2_counts[item] += 1

s = 0
for key, value in l1_counts.items():
	s += value * key * l2_counts.get(key, 0)
print(s)