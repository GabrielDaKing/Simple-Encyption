import tkinter as TK
import encryption

def display_encrypted(txt,ent):
	print ("Encrypted Message")
	txt.configure(state='normal')
	txt.delete(1.0, TK.END )
	txt.update()
	txt.insert(TK.CURRENT , encryption.encode(ent.get()))
	txt.configure(state='disabled')

def display_decrypted(txt,ent):
	print ("Decrypted Message")
	txt.configure(state='normal')
	txt.delete(1.0, TK.END )
	txt.update()
	txt.insert(TK.CURRENT , encryption.decrypt(ent.get()))
	txt.configure(state='disabled')

def main():
	root = TK.Tk()
	text_frame = TK.Frame(root)
	button_frame = TK.Frame(root)
	
	display_message = TK.Text(text_frame, state='disabled', height=2,width=60)
	enter_essage = TK.Entry(text_frame,width=80)
	display_message.pack()
	enter_essage.pack( )
	encrypt = TK.Button(button_frame,activeforeground="green",
	text="Encypt",command= lambda : display_encrypted(display_message,enter_essage))
	decrypt = TK.Button(button_frame,activeforeground="Green",
	text="Decypt",command= lambda : display_decrypted(display_message,enter_essage))
	exit_button = TK.Button(button_frame,activeforeground="red",
	text="Exit",command= lambda : exit())
	encrypt.pack(side = TK.LEFT)
	decrypt.pack(side = TK.LEFT)
	exit_button.pack(side = TK.LEFT)

	text_frame.pack()
	button_frame.pack()

	'''
	display_message.place(anchor='n')
	enter_essage.place(anchor='n')
	encrypt.place(anchor='s')
	decrypt.place(anchor='s')
	exit_button.place(anchor='s')
	'''

	root.mainloop()

main()