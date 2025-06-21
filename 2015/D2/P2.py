with open('input.txt') as gifts_txt:
	gifts = [gift.strip().split('x') for gift in gifts_txt.readlines()]

s = 0
for gift in gifts:
	l, w, h = int(gift[0]), int(gift[1]), int(gift[2])
	v = l * w * h
	p = 2 * l + 2 * w + 2 * h - 2 * max(l, w, h)
	s += v + p
print(s)