"""
10. Đếm số dòng trong file

Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix.
"""
import sys

def line_count(filename):
	n = 0
	f = open(filename, 'rU')
	for line in f:
		n = n + 1
	f.close()
	return n

if __name__ == '__main__':
	filename = sys.argv[1]
	print(line_count(filename))
