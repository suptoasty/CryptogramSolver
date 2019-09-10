#!/usr/bin/env python3
import io
import re
import os
import types
import time

# common lists of word/letter orders in english
letter_order: list = ['e', 't', ['a', 'i', 'o', 'n', 's'], 'h', 'r', 'd', 'l', 'u', ['c', 'm'], 'f', ['w', 'y'], ['g', 'p'], 'b', 'v', 'k', 'q', ['j', 'x'], 'z' ]
single_letter_words: list = ['a', 'i']
two_letter_words: list = ['in', 'on', 'an', 'of', 'so', 'or', 'is', 'to', 'go', 'am', 'us', 'me', 'up', 'he', 'we' 'by', 'as', 'at', 'my', 'no']
diagraph_list_begin: list = ['ch', 'kn', 'ph', 'sh', 'th', 'wh', 'wr'] 
diagraph_list_end: list = ['ch', 'ck', 'sh', 'ss', 'tch']
vowel_diagraph_list: list = ['ai', 'ay', 'ee', 'ea', 'ie', 'oa', 'oe', 'ue', 'ui', 'oo']

# def encrypt(cipher:list, shift_amount: int)-> str:
# 	asc: list = [] # us as map of used characters
# 	word: str
# 	for word in cipher:
# 		pass
# 	return asc

# def is_solved(cipher: list, plaintext: list)-> bool:
# 	word: str
# 	for word in cipher:
# 		#if word is the same then cryptogram is not solved
# 		if(word in plaintext):
# 			return False
# 		#if characters at the same position are in both lists then not solved
# 		character: chr
# 		for character in word:
# 			return False
# 	return True

# solves cryptogram taken in as a list of words
def solve(cipher: list, use_i=False)-> list:
	partial_text: list = []
	plaintext: list = cipher.copy()
	# while not is_solved(cipher, plaintext):
	# 	break

	# dictionary makes it easy to index using current character
	frequency_table: dict = get_frequency_table(list_to_string(cipher))
	word_map: dict = {} # dict for storing which letters might be plain text letters
	frequency_table_ordered: list = sort_dictionary_by_value(frequency_table)

	# need to use frequency table on single letter words first
	last_letter = ''
	word: str
	for word in cipher:
		if(len(word)==1 and not word in word_map):
			last_letter = word
			if(use_i): word_map[word] = "i"
			else: word_map[word] = "a"
			
			# plaintext.append("a")
			# plaintext.append("i")

	# figure out how to replace letters in words in list
	for word in plaintext:
		if(word_map.get(word) is None):
			continue
		# word_freq: dict = get_frequency_table(word)
		# for i in word_freq.keys():
		# 	for n in frequency_table.keys():
		# 		if(i==n):
		# 			print("found same frequency at word: ", word)


		# if(len(word)==1):
		# 	word = word_map.get(word)
		# for characte in word:
		# 	if(characte == last_letter):
		# 		characte = word_map.get(characte)
		
	# then replace other letters in the cipher with a or i
	# move on to digraphs
	# check cipher for those digraphs
	# check for double ll, oo, etc
	
	# for word in cipher:
	# 	if(len(word)==2):
	# 		plaintext.append("2letter")
	# 	if(len(word)>2):
	# 		plaintext.append("3plus")
	return plaintext

def sort_dictionary_by_value(dictionary: dict)-> list:
	return sorted(dictionary, key=dictionary.get, reverse=True)

# takes string and makes frequency "table" of each character
def get_frequency_table(string: str)->dict:
	frequency_table: dict = {}
	character: chr
	for character in string:
		if(character in frequency_table):
			frequency_table[character] += 1
		else:
			frequency_table[character] = 1
	return frequency_table

# turns list of words into one string
def list_to_string(m_list: list)->str:
	return ''.join(str(i) for i in m_list)

# lambda/regex function for converting cipher to map of words then a more useful list after stripping undesired symbols
def text_to_list(text: str)-> list:
    return list(map(lambda x: re.sub("[,.!?]", "", x).lower(), text.split()))

# returns string instead of list for ui
def read_plain_text(file_name: str):
	file = open(file_name, 'r')
	text: str = file.read()
	file.close()
	return text

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
	# print(list_to_string(cipher))
	plaintext: list = solve(cipher, False)
	print("Plain Text Is: ")
	print_list(plaintext)
	# print_list(cipher)
	print("MSecs: ", int(round(time.time() * 1000))-time_before)