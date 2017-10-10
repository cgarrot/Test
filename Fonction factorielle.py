#Fonction_factorielle_&_recursive_fonction_factorielle

def fonction_factorielle(valeur):
	if valeur <= 1:
		return 1
	accumulateur = 1
	while valeur > 1:
		accumulateur = accumulateur * valeur
		valeur = valeur - 1
	return accumulateur

def recursive_fonction_factorielle(valeur):
	if valeur <= 1:
		return 1
	return valeur * recursive_fonction_factorielle(valeur - 1)