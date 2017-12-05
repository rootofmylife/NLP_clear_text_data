"""
04. Ký tự thành phần

    Tokenize câu sau: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    Lấy ra ký tự đầu tiên của các từ ở vị trí 1, 5, 6, 7, 8, 9, 15, 16, 19; với các từ còn lại lấy ra 2 ký tự đầu tiên. Tạo ra một map từ các xâu ký tự được trích ra tới vị trí của từ trong câu.
"""
from nltk.tokenize import word_tokenize
from pprint import pprint

if __name__ == '__main__':
	str_ex = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	words = word_tokenize(str_ex)
	
	char_dict = {}
	keys = [1, 5, 6, 7, 8, 9, 15, 16, 19]	
	index_dict = {key: None for key in keys}
	
	for i in range(len(words)):
		w = words[i]
		if i + 1 in index_dict:
			char_dict[w[0]] = i + 1
		else:
			char_dict[''.join(w[0:2])] = i + 1
	pprint(char_dict)
	
