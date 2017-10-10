def my_putchar(char):

	write(1, c, 1)

def get_last_line(size):

	l_count = 0
	e_count = 4
	star = 1
	offset = 2

	for tri in size:
		while (l_count < e_count):
			l_count = l_count + 1
			star = star + 2
		
		if ((l_count == e_count) & ((tri % 2) == 0)):
			star = star - offset
		elif ((l_count == e_count) & ((tri % 2) == 1)):
			star = star - offset
			offset = offset + 2
		
		l_count = 0
		e_count = e_count + 1
	
	return (star)

def gen_line_space(space):

	count = 0

	while (count < space):
		my_putchar(' ')
		count = count + 1
	
	space = space - 1
	return (space)

def gen_line_star(star):
	count = 0;

	while (count < star):
		my_putchar('*')
		count = count + 1
	
	star = star + 2
	return (star)

def gen_feuillage(size_last_line, size):
	space = size_last_line / 2
	star = 1
	e_count = 4
	l_count = 0
	offset = 1

	for tri in size:
		while (l_count < e_count):
			space = gen_line_space(space)
			star = gen_line_star(star)
			my_putchar('\n')
			l_count = l_count + 1
		
		space = (space + 1) + offset
		star = (star - 2) - (offset * 2)
		if (((tri % 2) == 0)):
			offset = offset + 1
		l_count = 0
		e_count = e_count + 1

def tree(size):
	line = size
	space = 0
	size_last_line = get_last_line(size)
	space_tronc = (size_last_line / 2) - (size / 2)
	counter = 0

	if(size < 1):
		return
	gen_feuillage(size_last_line, size)
	for counter in size:
		if((size % 2) == 0):
			line = line + 1
		for space in space_tronc:
			my_putchar(' ')
		while(line != 0):
			my_putchar('|')
			line = line - 1
		my_putchar('\n')
		line = size

def main(tree, gen_feuillage, my_putchar):
	tree(5)
	return
