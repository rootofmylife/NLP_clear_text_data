"""
05. n-gram

    Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (xâu ký tự hoặc danh sách).

    Sử dụng hàm đã viết, sinh ra word bi-gram và character bi-gram từ câu sau: "I am an NLPer"

"""
def get_ngrams(arr, n, delim = ''):
	ngrams = []
	for i in range(len(arr)):
		min = i
		max = n + min - 1
		if max >= len(arr):
			break
		ngrams.append(delim.join(arr[min:max + 1]))
	return ngrams

def get_char_ngrams(s, n):
	char = []
	char[:0] = s
	char.insert(0, '_BOS_')
	char.append('_EOS_')
	return get_ngrams(char, 2)

def get_word_ngrams(s, n):
	word = s.split()
	word.insert(0, '_BOS_')
	word.append('_EOS_')
	return get_ngrams(word, 2, '/')

if __name__ == '__main__':
	s = 'I am an NLPer'
	print(get_word_ngrams(s,2))
	print(get_char_ngrams(s,2))
