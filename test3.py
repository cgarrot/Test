import sys
w = sys.stdout.write


def feuillage():
	for i in range(4):
		for a in range(4-i):
			w(" ")
		w("*")
		for l in range(i<<1):
			if i==4:
				w("*")
			else:
				w("*")
		("*")
		print(" ")




feuillage()
