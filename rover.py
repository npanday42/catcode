import math

def turnradius(base, angle):
	return base / math.sin(math.radians(angle))

val = input('> ')
while val:
	val = str.split(val)
	base = float(val[0])
	dist = float(val[1])
	angle = float(val[2])
	turn = turnradius(base, angle)
	circ = 2 * math.pi * turn
	rad = dist / turn
	y = turn * math.sin(rad)
	x = turn * (1 - math.cos(rad))
	d = (dist / circ * 360) % 360
	print(round(x, 2), round(y, 2), round(d, 2))
	val = input('> ')
