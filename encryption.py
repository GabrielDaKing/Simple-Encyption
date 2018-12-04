import re
import json

def encrypt(message):
	#This converts the encoded word to an encrypted message

	final_message = ""
	with open('key.json') as f:
		data = json.load(f)

	message = str(message)

	if message[0].isdigit():
		for i in range(0,len(message)-1,2):
			final_message += data[message[i]+message[i+1]]
		if len(message)%2!=0:
			final_message += "M" + message[len(message)-1]
	else:
		final_message += "N" + message[0]
		for i in range(1,len(message)-1,2):
			final_message += data[message[i]+message[i+1]]
		if (len(message)-2)%2!=0 :
			final_message += "M" + message[len(message)-1]

	return final_message

def encode(message):
	#This converts the intial word to an encoded message

	middle_message = "" 
	length = len(message)
	for i in range(length):
		'''
		ord : converts a chracter to integer
		bin : converts an integer value to 
		split : divides a t=string based on a charcter
		zfill : adds zeroes to the string to accomodate thr right size
		'''
		middle_message += str(bin(ord(message[i])).split('b')[1].zfill(8))

	length2 = len(middle_message)
	middle_message2 = ""

	j=0
	while j < length2:
		c = 0
		if middle_message[j] == "0":
			while middle_message[j] == "0" and j < length2:
				c += 1
				j += 1
				if j >= length2 :
					break
			middle_message2 += "%.0f"%(c)
		else:  
			while middle_message[j] == "1" and j < length2:
				c += 1
				j += 1
				if j >= length2 :
					break
			middle_message2 += chr(c + 96)

	return encrypt(middle_message2)

def decode(middle_message2):
	#This function decodes the decrypted message

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
	#This fuction decrypts the encoded message

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

	return decode(middle_message2)