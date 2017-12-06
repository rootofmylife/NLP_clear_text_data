"""
06. Tập hợp

    Sinh ra tập X và Y tương ứng là tập các character bi-gram từ hai xâu ký tự "paraparaparadise" và "paragraph".

    Sinh ra các tập hợp union, intersection và difference của X và Y

    Kiểm tra xem bi-gram 'se' có thuộc tập X (Y) hay không?

"""

from sol_5 import get_char_ngrams

if __name__ == '__main__':
	s1 = 'paraparaparadise'
	s2 = 'paragraph'
	
	X = set(get_char_ngrams(s1, 2))
	Y = set(get_char_ngrams(s2, 2))

	union = X.union(Y)
	intersection = X.intersection(Y)
	difference = X.difference(Y)

	print(union)
	print(intersection)
	print(difference)
