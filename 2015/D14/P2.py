with open('input.txt') as lines_txt:
	lines = [line.strip().split() for line in lines_txt.readlines()]

speed_times = {(int(line[3]), int(line[6]), int(line[-2])): 0 for line in lines}

for t in range(1, 2504):
	lead_reindeer, max_distance = (), 0
	for speed_time in speed_times.keys():
		speed, fly, rest = speed_time
		distance = (t // (fly + rest)) * speed * fly
		time_left = t % (fly + rest)
		if time_left < fly: distance += speed * time_left
		else: distance += speed * fly
		if distance > max_distance:
			max_distance = distance
			lead_reindeer = speed_time
	speed_times[lead_reindeer] += 1
print(max(speed_times.values()))