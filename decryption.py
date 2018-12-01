import re
import json

def decode(middle_message2):

	middle_message = ""

	for j in range(len(middle_message2)):
		if middle_message2[j].isdigit() :
			for n in range(int(middle_message2[j])):
				middle_message += "0"
		else:
			for n in range(int(ord(middle_message2[j])-96)):
				middle_message += "1"

	semi_final_message = re.findall('........?', middle_message)			
	
	final_message = ""
	for letter in semi_final_message:
		final_message += chr(int(letter,2))

	return final_message

def decrypt(message):

	middle_message2 = ""
	length = len(message)
	binary_values = []

	with open('key.json') as f:
		data = json.load(f)

	for i in range(len(message)):
		if message[i]=="N" or message[i]=="M":
			i+=1;
			middle_message2 += message[i]
		else:
			middle_message2 += data[message[i]]

	return middle_message2

def main():
	message = ""
	message += input("Enter the message to be decrypted : ")

	message2 = decrypt(message)	
	final_message = decode(message2)

	print("This is the decrypted message : %s" %(final_message))	

main()