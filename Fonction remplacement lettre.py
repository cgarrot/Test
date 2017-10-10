#Fonction_remplacement_lettre

def convert_text(text):
	text = text.lower()

	d = {
			'e': ['é', 'è', 'ê', 'ë'],
			'a': ['à'],
			'c': ['ç'],
			'u': ['û', 'ü'],
			'o': ['ô', 'ö'],
			'i': ['î', 'ï'],
		}
	for char in d:
		for c in d[char]:
			code = text.replace(c, char)
	return text.upper()