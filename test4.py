import math

a = int(input('A?'))
b = int(input('B?'))
c = int(input('C?'))

delta = b ** 2 - 4 * a * c
print('Le discriminant est :', delta)

if delta > 0:
	sol1 = (-b + math.sqrt(delta)) / 2 * a
	print('Solution 1:', sol1)
	sol2 = (-b - math.sqrt(delta)) / 2 * a
	print('Solution 2:', sol2)
if delta == 0:
	sol3 = -b / 2 * a
	print('Solution 1:', sol3)
if delta < 0:
	sol4 = (-b + 1j * math.sqrt(-delta)) / 2 * a
	print('Solution 1:', sol4)
	sol5 = (-b - 1j * math.sqrt(-delta)) / 2 * a
	print('Solution 2:', sol5)