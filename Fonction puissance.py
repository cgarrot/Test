#Fonction puissance

def fonction_puissance(valeur, puissance):
	if puissance == 0:
		return 1
	if puissance == 1:
		return valeur

	temp = valeur
	while puissance !=1:
		temp = temp * valeur
		puissance = puissance - 1
	return temp