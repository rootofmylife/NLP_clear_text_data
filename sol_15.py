"""
15. Trích xuất ra N hàng cuối cùng của file

Viết chương trình trích xuất ra N hàng cuối cùng của file. Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N. Sử dụng lệnh tail trong unix để thực hiện công việc.
"""
import sys

def read_n_lines_bot(filename, n):
	f = open(filename, 'rU')
	i = len(f) - n
	for i in f:
		if i == len(f) - 1:
			break
		print(i)
		i = i + 1
	f.close()

if __name__ == '__main__':
	read_n_lines_bot(sys.argv[1], 5)	
