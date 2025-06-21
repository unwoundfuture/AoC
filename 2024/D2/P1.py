with open('input.txt') as reports_txt:
	reports = [[int(i) for i in report.split()] for report in reports_txt.readlines()]

def is_safe(l):
	safe = True
	increasing = ((l[1] - l[0]) > 0)
	for i in range(1, len(l)):
		d = l[i] - l[i - 1]
		if d == 0 or (d > 0) != increasing or abs(d) > 3:
			safe = False
			break
	return safe

s = 0
for report in reports:
	if is_safe(report): s += 1
print(s)