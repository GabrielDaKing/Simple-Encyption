import re
import json




def main():
	message = input("Enter the message to be ecrypted : ")
	middle_message = "" 
	length = len(message)
	binary_values = []
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

	final_message = ""

	#everything thing below this converts coding into encryption

	with open('key.json') as f:
		data = json.load(f)

	if middle_message2[0].isdigit():
		for i in range(0,len(middle_message2)-1,2):
			final_message += data[middle_message2[i]+middle_message2[i+1]]
		if len(middle_message2)%2!=0:
			final_message += "M" + middle_message2[len(middle_message2)-1]
	else:
		final_message += "N" + middle_message2[0]
		for i in range(1,len(middle_message2)-1,2):
			final_message += data[middle_message2[i]+middle_message2[i+1]]
		if (len(middle_message2)-2)%2!=0 :
			final_message += "M" + middle_message2[len(middle_message2)-1]

	print(middle_message2)
	print(final_message)


main()