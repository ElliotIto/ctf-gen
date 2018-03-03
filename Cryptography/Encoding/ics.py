import re
from PIL import Image
import requests
import shutil
import os

# Python 3
# Uses Pillow

# ICS Information from https://en.wikipedia.org/wiki/International_Code_of_Signals
ICS_source = {'A': 'https://upload.wikimedia.org/wikipedia/commons/7/71/ICS_Alpha.svg',
	'B': 'https://upload.wikimedia.org/wikipedia/commons/f/f7/ICS_Bravo.svg',   
	'C': 'https://upload.wikimedia.org/wikipedia/commons/e/e7/ICS_Charlie.svg', 
	'D': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/ICS_Delta.svg',
	'E': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/ICS_Echo.svg',
	'F': 'https://upload.wikimedia.org/wikipedia/commons/a/a8/ICS_Foxtrot.svg',
	'G': 'https://upload.wikimedia.org/wikipedia/commons/f/fb/ICS_Golf.svg',
    'H': 'https://upload.wikimedia.org/wikipedia/commons/0/0f/ICS_Hotel.svg',
	'I': 'https://upload.wikimedia.org/wikipedia/commons/8/8e/ICS_India.svg',
	'J': 'https://upload.wikimedia.org/wikipedia/commons/a/a0/ICS_Juliet.svg',
	'K': 'https://upload.wikimedia.org/wikipedia/commons/a/a8/ICS_Kilo.svg',
	'L': 'https://upload.wikimedia.org/wikipedia/commons/7/76/ICS_Lima.svg',
	'M': 'https://upload.wikimedia.org/wikipedia/commons/7/73/ICS_Mike.svg',
	'N': 'https://upload.wikimedia.org/wikipedia/commons/2/21/ICS_November.svg',
	'O': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/ICS_Oscar.svg',
	'P': 'https://upload.wikimedia.org/wikipedia/commons/d/d0/ICS_Papa.svg',
	'Q': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/ICS_Quebec.svg',
	'R': 'https://upload.wikimedia.org/wikipedia/commons/b/bf/ICS_Romeo.svg',
	'S': 'https://upload.wikimedia.org/wikipedia/commons/3/36/ICS_Sierra.svg',
    'T': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/ICS_Tango.svg',
	'U': 'https://upload.wikimedia.org/wikipedia/commons/e/e2/ICS_Uniform.svg',
	'V': 'https://upload.wikimedia.org/wikipedia/commons/e/ef/ICS_Victor.svg',
	'W': 'https://upload.wikimedia.org/wikipedia/commons/8/88/ICS_Whiskey.svg',
    'X': 'https://upload.wikimedia.org/wikipedia/commons/b/ba/ICS_X-ray.svg',
	'Y': 'https://upload.wikimedia.org/wikipedia/commons/2/23/ICS_Yankee.svg',
	'Z': 'https://upload.wikimedia.org/wikipedia/commons/c/c6/ICS_Zulu.svg',
	'0': 'https://upload.wikimedia.org/wikipedia/commons/a/ac/ICS_Pennant_Zero.svg',
	'1': 'https://upload.wikimedia.org/wikipedia/commons/c/c1/ICS_Pennant_One.svg',
	'2': 'https://upload.wikimedia.org/wikipedia/commons/c/c0/ICS_Pennant_Two.svg',
	'3': 'https://upload.wikimedia.org/wikipedia/commons/6/64/ICS_Pennant_Three.svg',
	'4': 'https://upload.wikimedia.org/wikipedia/commons/8/87/ICS_Pennant_Four.svg',
	'5': 'https://upload.wikimedia.org/wikipedia/commons/a/ad/ICS_Pennant_Five.svg',
	'6': 'https://upload.wikimedia.org/wikipedia/commons/d/da/ICS_Pennant_Six.svg',
	'7': 'https://upload.wikimedia.org/wikipedia/commons/b/b8/ICS_Pennant_Seven.svg',
	'8': 'https://upload.wikimedia.org/wikipedia/commons/3/30/ICS_Pennant_Eight.svg',
	'9': 'https://upload.wikimedia.org/wikipedia/commons/2/2c/ICS_Pennant_Niner.svg'
        }


ICS = {'A': 'ICS_Alpha.svg',
	'B': 'ICS_Bravo.svg',   
	'C': 'ICS_Charlie.svg', 
	'D': 'ICS_Delta.svg',
	'E': 'ICS_Echo.svg',
	'F': 'ICS_Foxtrot.svg',
	'G': 'ICS_Golf.svg',
    'H': 'ICS_Hotel.svg',
	'I': 'ICS_India.svg',
	'J': 'ICS_Juliet.svg',
	'K': 'ICS_Kilo.svg',
	'L': 'ICS_Lima.svg',
	'M': 'ICS_Mike.svg',
	'N': 'ICS_November.svg',
	'O': 'ICS_Oscar.svg',
	'P': 'ICS_Papa.svg',
	'Q': 'ICS_Quebec.svg',
	'R': 'ICS_Romeo.svg',
	'S': 'ICS_Sierra.svg',
    'T': 'ICS_Tango.svg',
	'U': 'ICS_Uniform.svg',
	'V': 'ICS_Victor.svg',
	'W': 'ICS_Whiskey.svg',
    'X': 'ICS_X-ray.svg',
	'Y': 'ICS_Yankee.svg',
	'Z': 'ICS_Zulu.svg',
	'0': 'ICS_Pennant_Zero.svg',
	'1': 'ICS_Pennant_One.svg',
	'2': 'ICS_Pennant_Two.svg',
	'3': 'ICS_Pennant_Three.svg',
	'4': 'ICS_Pennant_Four.svg',
	'5': 'ICS_Pennant_Five.svg',
	'6': 'ICS_Pennant_Six.svg',
	'7': 'ICS_Pennant_Seven.svg',
	'8': 'ICS_Pennant_Eight.svg',
	'9': 'ICS_Pennant_Niner.svg'
        }


def ics_converter(ascii_string):
	"""Converts provided ascii string into an array of ICS flags"""
	ics_flags = []
	convert_ascii = ascii_string.upper()
	for letter in convert_ascii:
		if letter in ICS:
			ics_flags.append('Flag/' + ICS.get(letter))
		else:
			print("WARNING: \'{}\' in \"{}\" is not convertable!".format(letter, 
				ascii_string))
	return ics_flags


def image_creator(ics_flags,ascii_string):
	"""Creates image file from provided array of file names"""
	# Modified from https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
	images = map(Image.open, ics_flags)
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]
	file_name = ascii_string
	file_name += '.jpg'
	new_im.save(file_name)


def user_decision(user_input):
	"""Creates ICS image from either from stdin by user or file"""
	if user_input:
		ascii_string = input("Input to convert to ICS Flags: ")
		image_creator(ics_converter(ascii_string), ascii_string)

	else:
		while True:
			try:
				input_file = input("File path of txt file to convert: ")
				include_plain = input("Include plain text? (y/n): ")
				with open(var,"r") as ascii_file:
					for line in ascii_file:
						image_creator(ics_converter(line), line)
			except FileNotFoundError:
				print("File {} is not found.".format(input_file)) 


def collectFlagImages():
	"""Downloads Flag Images from Wikipedia"""

	# http://stackoverflow.com/questions/1274405/ddg#1274465
	if not os.path.exists('Flags'):
		os.makedirs('Flags')
	for item in ICS_source:
		# https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
		r = requests.get(ICS_source.get(item), stream=True)
		if r.status_code == 200:
			with open('Flags/' + ICS.get(item), 'wb') as f:
				for chunk in r.iter_content(1024):
					f.write(chunk)
			

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
