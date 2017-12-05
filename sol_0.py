"""
00. Đảo ngược xâu ký tự
Hãy đảo ngược xâu ký tự "stressed" (theo thứ tự từ cuối xâu đến đầu xâu ký tự).
"""

def reverse_string(s):
	return s[::-1]


if __name__ == '__main__':
	s = "stress"
	print(reverse_string(s))
