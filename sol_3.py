"""
03. Tokenize và thống kê số lượng ký tự của mỗi từ

    Tokenize câu sau: "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện của từ đó trong câu.

"""
from nltk.tokenize import word_tokenize
import re

#num of alphabet char in a string
def char_count(w):
	num = 0
	for i in range(len(w)):
		if re.search(r'[a-zA-Z]', w[i]):
			num = num + 1
	return num

def get_num_chars(words):
	list_str = []
	for w in words:
		list_str.append(char_count(w))
	return list_str

if __name__ == '__main__':
	sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	words = word_tokenize(sent)
	print(words)
	print("\n")
	print(get_num_chars(words))
