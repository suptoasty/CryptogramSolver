#!/usr/bin/env python3
import io
import re
import os
import types
import time
# import nltk

# common lists of word/letter orders in english
common_letter_list: list = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'q', 'j', 'x', 'z' ]
# single_letter_words: list = ['a', 'i']
two_letter_words: list = ['in', 'on', 'an', 'of', 'so', 'or', 'is', 'to', 'go', 'am', 'us', 'me', 'up', 'he', 'we' 'by', 'as', 'at', 'my', 'no']
diagraph_list_begin: list = ['ch', 'kn', 'ph', 'sh', 'th', 'wh', 'wr'] 
diagraph_list_end: list = ['ch', 'ck', 'sh', 'ss', 'tch']
vowel_diagraph_list: list = ['ai', 'ay', 'ee', 'ea', 'ie', 'oa', 'oe', 'ue', 'ui', 'oo']
# common_words_list: list = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "will", "an", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "when", "me", "make", "can", "like", "time", "no", "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]
common_words_list: list = ['as', 'i', 'his', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'by', 'hot', 'word', 'but', 'what', 'some', 'is', 'it', 'you', 'or', 'had', 'the', 'of', 'to', 'and', 'a', 'in', 'we', 'can', 'out', 'other', 'were', 'which', 'do', 'their', 'time', 'if', 'will', 'how', 'said', 'an', 'each', 'tell', 'does', 'set', 'three', 'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'any', 'new', 'work', 'part', 'take', 'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me', 'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form', 'sentence', 'great', 'think', 'say', 'help', 'low', 'line', 'differ', 'turn', 'cause', 'much', 'mean', 'before', 'move', 'right', 'boy', 'old', 'too', 'same', 'she', 'all', 'there', 'when', 'up', 'use', 'your', 'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over', 'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side', 'been', 'now', 'find', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', 'dont', 'while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose', 'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king', 'street', 'inch', 'multiply', 'nothing', 'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide', 'surface', 'deep', 'moon', 'island', 'foot', 'system', 'busy', 'test', 'record', 'boat', 'common', 'gold', 'possible', 'plane', 'stead', 'dry', 'wonder', 'laugh', 'thousand', 'ago', 'ran', 'check', 'game', 'shape', 'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring', 'yes', 'distant', 'fill', 'east', 'paint', 'language', 'among', 'unit', 'power', 'town', 'fine', 'certain', 'fly', 'fall', 'lead', 'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick', 'develop', 'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind', 'clear', 'tail', 'produce', 'fact', 'space', 'heard', 'best', 'hour', 'better', 'true', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table', 'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war', 'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve', 'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull', 'cold', 'notice', 'voice', 'energy', 'hunt', 'probable', 'bed', 'brother', 'egg', 'ride', 'cell', 'believe', 'perhaps', 'pick', 'sudden', 'count', 'square', 'reason', 'length', 'represent', 'art', 'subject', 'region', 'size', 'vary', 'settle', 'speak', 'weight', 'general', 'ice', 'matter', 'circle', 'pair', 'include', 'divide', 'syllable', 'felt', 'grand', 'ball', 'yet', 'wave', 'drop', 'heart', 'am', 'present', 'heavy', 'dance', 'engine', 'position', 'arm', 'wide', 'sail', 'material', 'fraction', 'forest', 'sit', 'race', 'window', 'store', 'summer', 'train', 'sleep', 'prove', 'lone', 'leg', 'exercise', 'wall', 'catch', 'mount', 'wish', 'sky', 'board', 'joy', 'winter', 'sat', 'written', 'wild', 'instrument', 'kept', 'glass', 'grass', 'cow', 'job', 'edge', 'sign', 'visit', 'past', 'soft', 'fun', 'bright', 'gas', 'weather', 'month', 'million', 'bear', 'finish', 'happy', 'hope', 'flower', 'clothe', 'strange', 'gone', 'trade', 'melody', 'trip', 'office', 'receive', 'row', 'mouth', 'exact', 'symbol', 'die', 'least', 'trouble', 'shout', 'except', 'wrote', 'seed', 'tone', 'join', 'suggest', 'clean', 'break', 'lady', 'yard', 'rise', 'bad', 'blow', 'oil', 'blood', 'touch', 'grew', 'cent', 'mix', 'team', 'wire', 'cost', 'lost', 'brown', 'wear', 'garden', 'equal', 'sent', 'choose', 'fell', 'fit', 'flow', 'fair', 'bank', 'collect', 'save', 'control', 'decimal', 'ear', 'else', 'quite', 'broke', 'case', 'middle', 'kill', 'son', 'lake', 'moment', 'scale', 'loud', 'spring', 'observe', 'child', 'straight', 'consonant', 'nation', 'dictionary', 'milk', 'speed', 'method', 'organ', 'pay', 'age', 'section', 'dress', 'cloud', 'surprise', 'quiet', 'stone', 'tiny', 'climb', 'cool', 'design', 'poor', 'lot', 'experiment', 'bottom', 'key', 'iron', 'single', 'stick', 'flat', 'twenty', 'skin', 'smile', 'crease', 'hole', 'jump', 'baby', 'eight', 'village', 'meet', 'root', 'buy', 'raise', 'solve', 'metal', 'whether', 'push', 'seven', 'paragraph', 'third', 'shall', 'held', 'hair', 'describe', 'cook', 'floor', 'either', 'result', 'burn', 'hill', 'safe', 'cat', 'century', 'consider', 'type', 'law', 'bit', 'coast', 'copy', 'phrase', 'silent', 'tall', 'sand', 'soil', 'roll', 'temperature', 'finger', 'industry', 'value', 'fight', 'lie', 'beat', 'excite', 'natural', 'view', 'sense', 'capital', 'wont', 'chair', 'danger', 'fruit', 'rich', 'thick', 'soldier', 'process', 'operate', 'practice', 'separate', 'difficult', 'doctor', 'please', 'protect', 'noon', 'crop', 'modern', 'element', 'hit', 'student', 'corner', 'party', 'supply', 'whose', 'locate', 'ring', 'character', 'insect', 'caught', 'period', 'indicate', 'radio', 'spoke', 'atom', 'human', 'history', 'effect', 'electric', 'expect', 'bone', 'rail', 'imagine', 'provide', 'agree', 'thus', 'gentle', 'woman', 'captain', 'guess', 'necessary', 'sharp', 'wing', 'create', 'neighbor', 'wash', 'bat', 'rather', 'crowd', 'corn', 'compare', 'poem', 'string', 'bell', 'depend', 'meat', 'rub', 'tube', 'famous', 'dollar', 'stream', 'fear', 'sight', 'thin', 'triangle', 'planet', 'hurry', 'chief', 'colony', 'clock', 'mine', 'tie', 'enter', 'major', 'fresh', 'search', 'send', 'yellow', 'gun', 'allow', 'print', 'dead', 'spot', 'desert', 'suit', 'current', 'lift', 'rose', 'arrive', 'master', 'track', 'parent', 'shore', 'division', 'sheet', 'substance', 'favor', 'connect', 'post', 'spend', 'chord', 'fat', 'glad', 'original', 'share', 'station', 'dad', 'bread', 'charge', 'proper', 'bar', 'offer', 'segment', 'slave', 'duck', 'instant', 'market', 'degree', 'populate', 'chick', 'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech', 'nature', 'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'quotient', 'teeth', 'shell', 'neck', 'oxygen', 'sugar', 'death', 'pretty', 'skill', 'women', 'season', 'solution', 'magnet', 'silver', 'thank', 'branch', 'match', 'suffix', 'especially', 'fig', 'afraid', 'huge', 'sister', 'steel', 'discuss', 'forward', 'similar', 'guide', 'experience', 'score', 'apple', 'bought', 'led', 'pitch', 'coat', 'mass', 'card', 'band', 'rope', 'slip', 'win', 'dream', 'evening', 'condition', 'feed', 'tool', 'total', 'basic', 'smell', 'valley', 'nor', 'double', 'seat', 'continue', 'block', 'chart', 'hat', 'sell', 'success', 'company', 'subtract', 'event', 'particular', 'deal', 'swim', 'term', 'opposite', 'wife', 'shoe', 'shoulder', 'spread', 'arrange', 'camp', 'invent', 'cotton', 'born', 'determine', 'quart', 'nine', 'truck', 'noise', 'level', 'chance', 'gather', 'shop', 'stretch', 'throw', 'shine', 'property', 'column', 'molecule', 'select', 'wrong', 'gray', 'repeat', 'require', 'broad', 'prepare', 'salt', 'nose', 'plural', 'anger', 'claim', 'continent']

# solves cryptogram taken in as a list of words
def solve(cipher: list, letter_mapping:dict = None)-> list:
	# common_words_list:list = read_text("words.txt")
	# nltk.download_shell()
	plaintext: list = cipher.copy()
	partial_text: list = []

	# dictionary makes it easy to index using current character
	letter_map: dict = {}
	if(not (letter_mapping is None)):
		letter_map = letter_mapping
	word_frequency_table:dict = sort_dictionary_by_value(get_frequency_table(plaintext))
	letter_frequency_table: dict = sort_dictionary_by_value(get_frequency_table(list_to_string(plaintext)))
	word_freq_list:list = list(word_frequency_table)
	letter_freq_list:list = list(letter_frequency_table)
	word_map: dict = {} # dict for storing which letters might be plain text letters

	used_words = []
	temp_letter_mapping: dict = {} #need to implement a map that can help me find starting letters so i don't have to hard code and rely on the word "the"
							 #should give only valid mappings for small words to the actual letter_map variable so, used letter map is not set to every character
	# for character in list_to_string(plaintext):
	# 	if(character not in temp_letter_mapping.keys()):
	# 		if(common_letter_list[letter_frequency_table.get(character)] in temp_letter_mapping.values()):
	# 			temp_letter_mapping[character] = common_letter_list[letter_frequency_table.get(character)-1%27]
	# 		else:
	# 			temp_letter_mapping[character] = common_letter_list[letter_frequency_table.get(character)%27]
	# temp_plain_text = plaintext.copy()
	# print(update_with_mapping(temp_plain_text, temp_letter_mapping))

	#check for diagraphs
	# for word in plaintext:
	# 	pass

	#find double letters
	has_double_letters = []
	for word in plaintext:
		for i in range(1, len(word)):
			if(word[i] == word[i-1]):
				has_double_letters.append(word)
				letter_map[word[i]] = common_letter_list[letter_frequency_table.get(word[i])]
				# temp:list = update_with_mapping(plaintext, letter_map)
				# plaintext = temp[0]
				# used_map = temp[1]
	
	single_letter_words = []
	for word in plaintext:
		if(len(word) is 1):
			if(word in single_letter_words):
				continue
			single_letter_words.append(word)
			# letter_map[word] = common_letter_list[letter_frequency_table.get(word)]
	character = ''
	i: int = 0
	for i in range(1, len(single_letter_words)):
		word = single_letter_words[i]	
		previous = single_letter_words[i-1]	
		if(letter_frequency_table.get(word)>letter_frequency_table.get(previous)):
			character = word
	if(character is not ''):
		letter_map[character] = common_letter_list[common_letter_list.index(character)]
		# temp:list = update_with_mapping(plaintext, letter_map)
		# plaintext = temp[0]
		# used_map = temp[1]

	# two most frequent are likely e then t, set them directly
	letter_map[letter_freq_list[0]] = 'e'
	temp:list = update_with_mapping(plaintext, letter_map)
	plaintext = temp[0]
	used_map = temp[1]

	letter_map[letter_freq_list[1]] = 't'

	temp:list = update_with_mapping(plaintext, letter_map)
	plaintext = temp[0]
	used_map = temp[1]

	#finish finding most common english word
	for word in plaintext:
		found = False
		if(not found):
			if(len(word) != 3):
				continue
			for common in common_words_list:
				# precent = SequenceMatcher(None, word, "the").ratio()
				percent = compare_words(word, common)
				if(percent >= 0.66):
					i = 0
					for i in range(len(word)):
						if(word[i] != common[i] and word[i] not in letter_map):
							letter_map[word[1]] = common[i]
							found = True
							temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
							plaintext = temp[0]
							used_map = temp[1]
							break

	letter_frequency_table = sort_dictionary_by_value(get_frequency_table(list_to_string(plaintext)))
	letter_freq_list = list(letter_frequency_table)
	# #find what uses these letters as there mappings
	# letter_map['e'] = letter_freq_list[]
	# letter_map['t']



	#find two letter words mappings
	used_words = []
	sub = get_subset_of_length(plaintext, 2)
	for word in sub:
		# if(word in used_words):
		# 	continue
		if(word[0] in letter_map.values()):
			if(word[0] is 't'):
				letter_map[word[1]] = 'o'
				temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
				plaintext = temp[0]
				used_map = temp[1]
			# elif(word[1] is 'e'):
			# 	letter_map[word[1]] = 'o'
			# 	temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
			# 	plaintext = temp[0]
			# 	used_map = temp[1]
			elif(word[1] is get_key_by_value(letter_map, 'o')):
				i = (letter_freq_list.index(word[0])%27)
				letter_map[word[0]] = common_letter_list[i-1]
				temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
				plaintext = temp[0]
				used_map = temp[1]
			elif(word[0] is get_key_by_value(letter_map, 'o') and word[1] not in letter_map.keys()):
				i = (letter_freq_list.index(word[1])%27)
				letter_map[word[1]] = common_letter_list[i]
				temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
				plaintext = temp[0]
				used_map = temp[1]
			elif(word[1] is 'o' and 's' in letter_map.values() and 'n' in letter_map.values() and 'd' in letter_map.values() and 'g' in letter_map.values()):
				letter_map[word[0]] = 't'
				temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
				plaintext = temp[0]
				used_map = temp[1]
				

	#look for words that are more than 75% matchin current words
	used_words:list = []
	used_letters:list = []
	for word in plaintext:
		if(word in used_words):
			continue
		for common in common_words_list:
			if(len(word) is len(common) and common not in used_words):
				# precent = SequenceMatcher(None, common, word).ratio()
				percent = compare_words(word, common)
				if(percent >= 0.6):
					i: int = 0
					for i in range(len(word)):
						if(word[i] != common[i] and ((word[i] not in letter_map.keys() and word[i] not in letter_map.values() )and common[i] not in letter_map.values())):
							letter_map[word[i]] = common[i]
							used_words.append(common)
							used_words.append(word)
	# letter_map['y'] = 'f'
							temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
							plaintext = temp[0]
							used_map = temp[1]
					# print(common)
	# temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
	# plaintext = temp[0]
	# used_map = temp[1]

	
	print(letter_map)
	print(len(letter_map.keys()))


	pt = cipher.copy()
	temp = update_with_mapping(pt, letter_map)
	pt = temp[0]
	print(pt)
	# used_words:list = ["the"]
	used_words:list = []
	for word in plaintext:
		if(word in common_words_list):
			used_words.append(word)
	used_letters:list = []
	for word in pt:
		if(word in common_words_list):
			used_words.append(word)
		if(word in used_words):
			continue
		old_word = word
		new_word = old_word
		for common in common_words_list:
			if(len(word) is len(common) and common not in used_words):
				# precent = SequenceMatcher(None, common, word).ratio()
				percent = compare_words(word, common)
				if(percent >= 0.6):
					new_word = common
					used_words.append(common)
		pt[pt.index(old_word)] = new_word

	plaintext = pt

	# last minute trys
	letter_frequency_table: dict = sort_dictionary_by_value(get_frequency_table(list_to_string(plaintext)))
	word: str
	for word in plaintext:
		i = 0
		for i in range(len(word)):
			if(word[i] not in letter_map.keys() and (word[i] not in letter_map.values())):
				character = common_letter_list[letter_frequency_table.get(word[i])]
				new_word = word.replace(word[i], character)
				if(new_word in common_words_list and character not in letter_map.values()):
					letter_map[word[i]] = character
					temp = update_with_mapping(plaintext, letter_map, used_letter_mapping=used_map)
					plaintext = temp[0]
					used_map = temp[1]
	# print("Is close to actual plaintext: ", validate_plaintext(plaintext, letter_map))

	return [plaintext, letter_map]

def validate_plaintext(plaintext: list, letter_mapping: dict = None)-> bool:
	word_count = len(plaintext)
	summation: int = 0
	for word in plaintext:
		if(word in common_words_list):
			summation += 1
	if(summation/word_count >= 0.75):
		return True
	else:
		return False

def get_key_by_value(dictionary: dict, value):
	# keys:list = list()
	key = None
	items = dictionary.items()
	for item in items:
		if(item[1] is value):
			# keys.append(item[0])
			key = item[0]
			break
	return key

def get_subset_of_length(list: list, size: int)-> list:
	sub: list = []
	for i in list:
		if(i in sub):
			continue
		if(len(i) is size):
			sub.append(i)
	return sub

def compare_words(word: str, word2: str)-> float:
	if(len(word) is not len(word2)): return 0.0
	sim: float = 0.0
	for i in range(len(word)):
		if(word[i] is word2[i]):
			sim += 1.0
	return sim / len(word)

#replace letters with those in map using in place modification, used_letter_mapping is optional and prevents remapping on second function call
def update_with_mapping(plaintext: list, letter_mapping: dict, used_letter_mapping=None)-> list:
	if(used_letter_mapping is not None):
		for character in letter_mapping.keys():
			if(character not in used_letter_mapping.keys()):
				plaintext = [item.replace(character, letter_mapping.get(character)) for item in plaintext]
				used_letter_mapping[character] = letter_mapping.get(character)
		return [plaintext.copy(), used_letter_mapping.copy()]
	for character in letter_mapping.keys():
		plaintext = [item.replace(character, letter_mapping.get(character)) for item in plaintext]
	return [plaintext.copy(), letter_mapping.copy()]

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

	temp = solve(cipher)
	plaintext: list = temp[0].copy()
	letter_map: dict = temp[1].copy()
	# while(not validate_plaintext(plaintext, letter_map)):
	#  	plaintext = solve(plaintext.copy())

	print("Plain Text Is: ", plaintext)
	print("Skewed Due to Sentinel!!!-> MSecs: ", int(round(time.time() * 1000))-time_before)
