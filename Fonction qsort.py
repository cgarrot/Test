#Fonction_qsort

def qsort(lst):
	if lst == []: return []
	pivot = lst[0]
	return qsort([x for x in lst[1:] if x<pivot]) + [pivot] + qsort([x for x in lst[1:] if x>=pivot])