"""
11. Biến đổi các ký tự tab thành space

Chuyễn mỗi ký tự tab thành ký tự space. Xác nhận kết quả lần lượt bằng các lệnh sed, tr, và expand.
"""
import sys

def convert_tab_2_space(filename):
	f = open(filename, 'rU')
	for line in f:
		re.sub(r'\t', ' ', line)
	f.close()

if __name__ == '__main__':
	file_name = sys.argv[1]
	convert_tab_2_space(file_name)
