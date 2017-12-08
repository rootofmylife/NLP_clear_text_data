"""
12. Lưu cột 1 vào file col1.txt, cột 2 vào file col2.txt

Trích xuất nội dung trong cột 1, cột 2 và lưu vào các file tương ứng: col1.txt và col2.txt. Thử thực hiện công việc chỉ dùng lệnh cut trong unix.
"""
import sys

def ext_column(src, dst, n):
	# n = cot can tach ra
	input = open(src, 'rU')
	output = open(dst, 'w')

	for line in fin:
		line = line.rstrip()
		cols = line.split()
		col = cols[n - 1]
		output.write(col)
		output.write("\n")

	input.close()
	output.close()

if __name__ == '__main__':
	file_name = sys.argv[1]
	ext_column(file_name, "dest_1.txt", 1)
	ext_column(file_name, "dest_2.txt", 2)
