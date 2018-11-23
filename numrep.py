"""
Author: Noah Abe
Program Name: numrep (NUMber REPresentation)
Date: Wed Oct 10 14:03:59 CDT 2018
Description: Changes a number from one base representation to another.
Acceptable bases for now are: base2(binary), base8(octal), base10(decimal) and
base16(hexadecimal). It also includes a functionality that can change a character
into its ASCII code.
Hope it will serve your needs!! Peace 0ut!!
"""

import argparse

def convert_to_decimal(number,base):
	###########[FOR HEXADECIMAL ONLY]############
	if base == 16:
	        convertion_table = {
        	        'A':10,
                	'B':11,
                	'C':12,
                	'D':13,
                	'E':14,
                	'F':15,
        	}
        	CONVERT = lambda x:convertion_table[x.upper()]
	#############################################
	decimal = 0
	position = len(number)-1
	for single_digit in number:
		if single_digit.isalpha():
			single_digit = CONVERT(single_digit)
		decimal += int(single_digit) * base**position
		position -= 1
	return decimal 


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='tell me a number and i will tell you a story')
	parser.add_argument('-b','--binary',
                action='store',
                type=str,
                dest='binary',
                default=None,
                help='specify the binary number',
        )
	parser.add_argument('-o','--octal',
                action='store',
                type=str,
                dest='octal',
                default=None,
                help='specify the octal number',
        )
	parser.add_argument('-d','--decimal',
                action='store',
                type=int,
                dest='decimal',
                default=None,
                help='specify the decimal number',
        )
	parser.add_argument('-hex','--hexadecimal',
                action='store',
                type=str,
                dest='hex',
                default=None,
                help='specify the hexadecimal number',
        )
	parser.add_argument('-c','--character',
                action='store',
                type=str,
                dest='char',
                default=None,
                help='specify the character value',
        )
	values = parser.parse_args()
	pure_number = None
	if values.binary is not None: pure_number = convert_to_decimal(values.binary,2)
	elif values.octal is not None: pure_number = convert_to_decimal(values.octal,8)
	elif values.decimal is not None: pure_number = values.decimal
	elif values.hex is not None: pure_number = convert_to_decimal(values.hex,16)
	elif values.char is not None: pure_number = ord(values.char)
	else:
		print("Use -h or --help for more information about numrep!!")
		exit()

	def convert_to_char(x):
		x_char = None
		try:
			x_char = chr(x)
		except OverflowError as err:
			x_char = str(err)
		except ValueError as err:
			x_char = str(err)
		return x_char

	output_data = {
		'BINARY':bin(pure_number),
		'OCTAL':oct(pure_number),
		'DECIMAL':pure_number,
		'HEXADECIMAL':hex(pure_number),
		'CHARACTER': convert_to_char(pure_number),
	}
	
	for name,value in output_data.items():
		print("{}: {}".format(name,value))

