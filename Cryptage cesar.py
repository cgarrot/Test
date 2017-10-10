#Cryptage_cesar

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
	text = input("Entrer le message: ")
	deca = int(input("Entrer le décalage: "))
	message = cesar(text,deca)
	print("Le message codé est: \n",message)

def cesar(text, deca):
	text = convert_text(text)
	new_text = ""

	for char in text:
		if char in ALPHABET:
			new_text += swap(char, deca)
		else:
			new_text += char
	return new_text

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

def swap(char, deca):
	index = ALPHABET.find(char)
	return ALPHABET[(index + deca) % 26]

if __name__ == '__main__':
	main()