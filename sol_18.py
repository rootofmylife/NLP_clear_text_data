"""
18. Sắp xếp các hàng theo thứ tự giảm dần của giá trị (numeric value) của cột thứ 3

Viết chương trình thực hiện nhiệm vụ trên. Dùng lệnh sort để xác nhận (trong bài tập này, kết quả của chương trình của bạn với lệnh sort có thể khác nhau do có thể có các giá trị giống nhau trong cột thứ 3).
"""

import numpy as np
import sys

def sort_by_col(filename):
	f = open(filename, 'rU')
	
	keys = []
	lines = []

	for line in f:
		line = line.rstrip()
		col = line.split()
		val = int(col[2])
		keys.append(val)
		lines.append(line)
	
	f.close()

	indexes = sorted(range(len(keys)), key = lambda x:keys[x], reverse=True)
	for i in indexes:
		print(lines[i])

if __name__ == '__main__':
	sort_by_col(sys.argv[1])
