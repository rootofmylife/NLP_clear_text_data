"""
17. Đưa ra các các xâu ký tự duy nhất (unique) trong cột 1

Đưa ra các xâu ký tự duy nhất trong cột 1 của file. Sử dụng lệnh cut, sort, uniq để thực hiện nhiệm vụ.
"""
import sys

def unique_strings(filename, n):
	f = open(filename, 'rU')
	strdict = {}
	for line in f:
		line = line.rstrip()
		cols = line.split()
		col = cols[n - 1]
		strdict[col] = None
	
	f.close()
	
	for key in sorted(strdict.keys()):
		print(key)

if __name__ == '__main__':
	unique_strings(sys.argv[1], 1)
