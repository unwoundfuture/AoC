with open('input.txt') as lines_txt:
	lines = [line.strip().split() for line in lines_txt.readlines()]

speed_times = [(int(line[3]), int(line[6]), int(line[-2])) for line in lines]

max_distance = 0
for speed_time in speed_times:
	speed, fly, rest = speed_time
	distance = (2503 // (fly + rest)) * speed * fly
	time_left = 2503 % (fly + rest)
	if time_left < fly: distance += speed * time_left
	else: distance += speed * fly
	if distance > max_distance: max_distance = distance
print(max_distance)