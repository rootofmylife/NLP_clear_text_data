"""
14. Trích xuất ra N hàng đầu tiên của file

Viết chương trình trích xuất ra N hàng đầu tiên của file. Biến số dạng dòng lệnh là số tự nhiên N. Sử dụng lệnh head trong unix để thực hiện công việc.
"""
import sys

def read_n_lines(filename, n):
	f = open(filename, 'rU')
	for i in range(n):
		print(f[i].readline())

	f.close()

if __name__ == '__main__':
	read_n_lines(sys.argv[1], 5)
