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

	return middle_message2

def main():
	message = input("Enter the message to be ecrypted : ")

	message2 = encode(message)
	final_message = encrypt(message2)

	print("This is the encrypted message : %s" %(final_message))	

main()