import math

pi = math.pi

def turnradius(base, angle):
	return base / math.sin(math.radians(angle))

def	vector(base, dist, angle):
	if angle == 0:
		return (0, dist, 0, 0)
	turn = turnradius(base, angle)
	circ = 2 * math.pi * turn
	angle = dist / turn
	x = turn * (1 - math.cos(angle))
	y = turn * math.sin(angle)
	dir = (dist / circ * 360) % 360
	return (x, y, dir, angle)

val = input('> ')
while val:
	val = str.split(val)
	x, y = 0, 0
	dir = 0
	base = float(val[0])
	path = val[2:]
	for dist, angle in zip(path[::2], path[1::2]):
		dist, angle = float(dist), float(angle)
		if dist < 0:
			angle = 180 - angle
		xx, yy, ddir, rad = vector(base, abs(dist), angle)
		hyp = math.hypot(xx, yy)
		angle = ((pi - rad) / 2) - math.radians((dir, dir + 180)[dist < 0])
		x += hyp * math.cos(angle)
		y += hyp * math.sin(angle)
		dir = (dir + ddir) % 360
	print(round(x, 2), round(y, 2), round(dir, 2))
	val = input('> ')
