import io
import re

def read_text(file_name: str)-> list:
	file = open(file_name, 'r')
	text: str = file.read()
	file.close()
	return text_to_list(text)

def text_to_list(text: str)-> list:
    return list(map(lambda x: re.sub("[,.!?]", "", x).lower(), text.split()))

def save_file(l: list):
    file = open("python_list_wrods.txt", "w")
    file.write(str(l))
    file.close()

if __name__ == "__main__":
    words = read_text("common_words.txt")
    save_file(words)
