import re

# Python 3

# Modified from https://stackoverflow.com/questions/32094525/morse-code-to-english-python3
MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        ' ': '/' 
        # ' ': '|'  #If one wants to use | instead of / for spaces
        }

def morse_converter(ascii_string):
	"""Converts ascii input into morse string"""
	morse_string = ""
	convert_ascii = ascii_string.upper()
	for letter in convert_ascii:
		if letter in MORSE:
			morse_string += MORSE.get(letter)
		else:
			print("WARNING: \'{}\' in \"{}\" is not convertable!".format(letter, 
				ascii_string))
		if letter is not " ":
			morse_string +=  " "
	return morse_string


def user_decision(user_input):
	"""Converts stdin or file into morsecode"""
	if user_input:
		ascii_string = input("Word to convert to morse: ")
		print("{} {}".format(ascii_string, morse_converter(ascii_string)))
	else:
		while True:
			try:
				input_file = input("File path of txt file to convert: ")
				output_file = input_file[:-3] + "-morse.txt"
				include_plain = input("Include plain text? (y/n): ")
				with open(var,"r") as ascii_file:
					for line in ascii_file:
						with open(output_file, "a") as output:
							if include_plain.lower() == 'y':
								output.write(line, morse_converter(line))
								output.write('\n')
								output.close()
							else:
								output.write(morse_converter(line))
								output.write('\n')
								output.close()
			except FileNotFoundError:
				print("File {} is not found.".format(input_file)) 
							
def main():
	user_input = -1
	while True:
		var = input("Single (1) or file input (0)?: ")
		if var.isdigit() and (int(var) == 1 or int(var) == 0):
			user_input = int(var)
			break
		else:
			print("Please enter 1 or 0")
	user_decision(int(var))

if __name__ == '__main__':
	main()