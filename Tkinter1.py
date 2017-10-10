from tkinter import *

main = Tk()
main.geometry("500x500")
main.title('Test')
main['bg'] = 'grey'

def hello():
	label['text'] = salude.get()


salude = StringVar()

label = Label(main)
label.pack()
texte = Entry(main, textvariable = salude).place(x = '300', y = '220')
bouton1 = Button(main, text= 'Bouton', command = hello).place(x = '400', y = '220')
