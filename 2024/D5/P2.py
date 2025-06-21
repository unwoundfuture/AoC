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

def correct_page_order(o):
	indexes = {o[i]: i for i in range(len(o))}
	for i in range(len(o) - 1):
		for page in rules[o[i]]:
			page_index = indexes.get(page, -1)
			if page_index > i:
				o.remove(page)
				o.insert(i, page)
				correction = correct_page_order(o)
				if correction == -1: return o[len(o) // 2]
				else: return correction
	return -1

s = 0
for order in orders:
	median = correct_page_order(order)
	if median != -1: s += median
print(s)