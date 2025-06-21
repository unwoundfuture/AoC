with open('input.txt') as gifts_txt:
	gifts = [gift.strip().split('x') for gift in gifts_txt.readlines()]

s = 0
for gift in gifts:
	l, w, h = int(gift[0]), int(gift[1]), int(gift[2])
	a1, a2, a3 = l * w, l * h, w * h
	s += 2 * (a1 + a2 + a3) + min(a1, a2, a3)
print(s)