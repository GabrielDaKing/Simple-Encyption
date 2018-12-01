import re

def main():
	message = ""
	message += input("Enter the message to be decrypted : ")
	middle_message = ""
	length = len(message)
	binary_values = []

	j=0
	for j in range(length):
		c = 0
		if message[j].isdigit() :
			for n in range(int(message[j])):
				middle_message += "0"
		else:
			for n in range(int(ord(message[j])-96)):
				middle_message += "1"

	semi_final_message = re.findall('........?', middle_message)			
	
	final_message = ""
	for letter in semi_final_message:
		final_message += chr(int(letter,2))

	#print(middle_message)
	#print(semi_final_message)
	print(final_message)
	

main()