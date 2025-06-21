with open('input_page_order_rules.txt') as order_rules_file:
	order_rules = order_rules_file.readlines()
rules = {}
for order_rule in order_rules:
	order_rule.strip('\n')
	x, y = order_rule.split('|')
	x, y = int(x), int(y)
	rules.setdefault(y, [])
	rules[y].append(x)

with open('input_page_orders.txt') as page_orders_file:
	page_orders = page_orders_file.readlines()
orders = []
for page_order in page_orders:
	page_order.strip('\n')
	orders.append([int(i) for i in page_order.split(',')])

s = 0
for order in orders:
	correct = True
	indexes = {order[i]: i for i in range(len(order))}
	for i in range(len(order) - 1):
		for page in rules[order[i]]:
			page_index = indexes.get(page, -1)
			if page_index > i:
				correct = False
				break
		if not correct: break
	if correct: s += order[len(order) // 2]
print(s)