#Cryptage_cesar2

def main():
	text = input("Entrer le message: ")
	deca = int(input("Entrer le décalage: "))
	message = cesar(text,deca)
	print("Le message codé est: \n",message)

def cesar(text, deca):
	new_text = ""

	for char in text:
		if(char.islower()):
			new_text += chr((ord(char) - ord('a') + deca) % 26 + ord('a'))
		elif(char.isupper()):
			new_text += chr((ord(char) - ord('A') + deca) % 26 + ord('A'))
		else:
			new_text += char
	return new_text

if __name__ == '__main__':
	main()