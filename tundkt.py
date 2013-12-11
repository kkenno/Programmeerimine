import math
a=raw_input('a: ')
b=raw_input('b: ')
c=raw_input('c: ')

a = int(a)
b = int(b)
c = int(c)

def ruut(a, b, c):

	d= b**2-4*a*c
	if d < 0:
		print "lahendid puuduvad"
	elif d == 0:
		x = (-b+math.sqrt(b**2-4*a*c))/2*a
		print "vastus :", x
	else:
		x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
		x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
		print "vastus :", x1, "ja", x2

ruut(a, b, c)
