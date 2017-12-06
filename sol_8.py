"""
08. Xâu mật mã

Từ các ký tự của một xâu cho trước, cài đặt hàm có tên cipher để mã hoá xâu như sau:

    Nếu là ký tự tiếng Anh ở dạng thường (lower-case characters) thì chuyển thành ký tự có mã là (219 - mã ký tự).
    Các ký tự khác giữ nguyên.

Sử dụng hàm đã viết để mã hoá và giải mã các xâu ký tự tiếng Anh.
"""
import re

def cipher(s):
	news = ""
	for i in range(len(s)):
		newc = s[i]
		if re.search(r'[a-z]', s[i]):
			newc = chr(219 - ord(s[i]))
		news = news + newc
	return news

def decipher(s):
	news = ""
	for i in range(len(s)):
		newc = s[i]
		if re.search(r'[a-z]', s[i]):
			newc = chr(219 - ord(s[i]))
		news = news + newc
	return news

if __name__ == '__main__':
	s = "aNh DuC"
	z = cipher(s)
	print(decipher(z))
