#!/usr/bin/env python3
import io
import re
import os
import types
import time
import binascii
import sys

# if sys.version_info[0] > 2:
#     print("Please use python3 or higher")
#     sys.exit(1)
# import importlib

# moduleName = input('Decrypt')
# importlib.import_module('Decrypt')

previous_shifts: list = [0] #store the previous shifts tested when decrypting

def encrypt(cipher:list, shift_amount: int)-> str:
	asc: list = []
	word: str
	for word in cipher:
		# asc.append(word.encode("ascii", "replace"))
		character: chr
		for character in word:
			# print(character.encode("ascii", "replace"))
			print(binascii.a2b_base64(word))
	return asc

def is_solved(cipher: list, plaintext: list)-> bool:
	word: str
	for word in cipher:
		#if word is the same then cryptogram is not solved
		if(word in plaintext):
			return False
		#if characters at the same position are in both lists then not solved
		character: chr
		for character in word:
			return False
	return True

"""
Solve using 
"""
def solve(cipher: list)-> list:
	plaintext: list = []
	while not is_solved(cipher, plaintext):
		break
	plaintext.append("need")
	plaintext.append("to")
	plaintext.append("actual")
	plaintext.append("solve")
	return plaintext

# lambda/regex function for converting cipher to map of words then a more useful list after stripping undesired symbols
def text_to_list(text: str)-> list:
    return list(map(lambda x: re.sub("[,.!?]", "", x).lower(), text.split()))
    """
    *Sorry for the bad form of multiline string as a comment and for the long comment*
    I think this runs in O(x)? My lambda calculus skills are non existant and my Big O are minimal
    You're probably millennia ahead of what my Algorithm Analysis skills could ever be Prof. Nix
    If you could take the time to tell me what this actually runs at, that would be appreciated
    """

# read text from file
def read_text(file_name: str)-> list:
	file = open(file_name, 'r')
	text: str = file.read()
	file.close()
	return text_to_list(text) # doest this prevent garbage collection on text??

# read from console
def read_console()-> list:
    return text_to_list(input("Input Text: "))


# prints words without newline
def print_list(cipher: list):
	word: str
	for word in cipher:
		print(word, end=" ")


if __name__ == "__main__":
	time_before: int = int(round(time.time() * 1000))
	use_file: bool = None
	while True:
		text: str = input("Would you like to use a file (y/n): ")
		if(text.lower() in ['y', 'yes', 'true']):
			use_file = True
			break
		elif(text.lower() in ['n', 'no', 'false']):
			use_file = False
			break
		else:
			print("Please Try again using Yes or No: ")
	cipher: list = None
	if(use_file):
		while True:
			file: str = input("File Path (Local or Global): ")
			if(os.path.exists(file)):
				cipher = read_text(file)
				break
			else:
				print("Invlaid File Path Try Again: ")
	else:
		cipher = read_console()
	plaintext: list = solve(cipher)
	print_list(cipher)
	print("MSecs: ", int(round(time.time() * 1000))-time_before)