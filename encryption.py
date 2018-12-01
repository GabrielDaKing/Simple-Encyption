import re

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
	final_message = ""


	j=0
	while j < length2:
		c = 0
		if middle_message[j] == "0":
			while middle_message[j] == "0" and j < length2:
				c += 1
				j += 1
				if j >= length2 :
					break
			final_message += "%.0f"%(c)
		else:
			while middle_message[j] == "1" and j < length2:
				c += 1
				j += 1
				if j >= length2 :
					break
			final_message += chr(c + 96)
	print(final_message)

main()