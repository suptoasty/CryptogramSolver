#!/usr/bin/env python3
import io
import re
import os
import types
import time

# common lists of word/letter orders in english
common_letter_list: list = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'q', 'j', 'x', 'z' ]
single_letter_words: list = ['a', 'i']
two_letter_words: list = ['in', 'on', 'an', 'of', 'so', 'or', 'is', 'to', 'go', 'am', 'us', 'me', 'up', 'he', 'we' 'by', 'as', 'at', 'my', 'no']
diagraph_list_begin: list = ['ch', 'kn', 'ph', 'sh', 'th', 'wh', 'wr'] 
diagraph_list_end: list = ['ch', 'ck', 'sh', 'ss', 'tch']
vowel_diagraph_list: list = ['ai', 'ay', 'ee', 'ea', 'ie', 'oa', 'oe', 'ue', 'ui', 'oo']
common_words_list: list = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "will", "an", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "when", "me", "make", "can", "like", "time", "no", "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]

# solves cryptogram taken in as a list of words
def solve(cipher: list, use_i=False)-> list:
	plaintext: list = cipher.copy()
	partial_text: list = []

	# dictionary makes it easy to index using current character
	word_frequency_table:dict = sort_dictionary_by_value(get_frequency_table(plaintext))
	letter_frequency_table: dict = sort_dictionary_by_value(get_frequency_table(list_to_string(plaintext)))
	word_freq_list:list = list(word_frequency_table)
	letter_freq_list:list = list(letter_frequency_table)
	word_map: dict = {} # dict for storing which letters might be plain text letters
	letter_map: dict = {}

	# character: chr
	# word: str
	# for word in plaintext:
	# 	for character in word:
	# 		old_char = character
	# 		character = common_letter_list[letter_freq_list.index(character)%26]
	# 		word = word.replace(old_char, character)
	# 		if(old_char not in word_map):
	# 			word_map[old_char] = character
	# 	partial_text.append(word)
	# print(word_map)

	#use letter map to prevent wrong words being chosen
	for word in plaintext:
		old_word = word
		if(old_word not in word_map):
			new_word = common_words_list[word_freq_list.index(word)%len(common_words_list)]
			if(len(old_word) is len(new_word)):
				for i in old_word:
					if(i not in letter_map and new_word[old_word.index(i)] not in letter_map.values()):
						letter_map[i] = new_word[old_word.index(i)]
				partial_text.append(new_word)
				word_map[old_word] = new_word
	
	character: chr
	word: str
	for word in plaintext:
		old_word = word
		if(word in word_map):
			continue
		new_word
		for character in word:
			new_word = word.replace(character, common_letter_list[letter_freq_list.index(character)%26])
		if(len(old_word) is len(new_word)):
			partial_text.append(word)
			word_map[old_word] = new_word
	print(letter_map)
	print(word_map)

	# letters when looking at word_map can have two mappings, need a way to prevent this to narrow down results

	plaintext = partial_text
	return plaintext

# uses for loop and sorted to order a dictionary by value
def sort_dictionary_by_value(dictionary: dict)-> dict:
	tab: dict = {}
	for i in sorted(dictionary, key=dictionary.get, reverse=True):
		tab[i] = dictionary[i]
	return tab
	# return sorted(dictionary, key=dictionary.get, reverse=True)

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

def get_word_frequency_table(l: list)-> dict:
	freq = [l.count(p) for p in l]
	return dict(zip(l, freq))

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

# cli drive for this script
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
	print("Plain Text Is: ", plaintext)
	# print_list(cipher)
	print("Skewed Due to Sentinel!!!-> MSecs: ", int(round(time.time() * 1000))-time_before)