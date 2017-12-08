"""
19. Sắp xếp theo tần suất xuất hiện

Đưa ra tần suất xuất hiện của các giá trị trong cột 1; sắp xếp các giá trị trong cột 1 theo thứ tự từ cao đến thấp của tần suất xuất hiện. Chỉ dùng lệnh cut, uniq, sort để thực hiện nhiệm vụ.
"""
import sys

def sort_by_colfreq(filename, n):
	f = open(filename, 'rU')
	
	colfreq = {}
	for line in f:
		line = line.rstrip()
		cols = line.split()
		val = cols[n - 1]
		if colfreq.has_key(val):
			colfreq[val] = colfreq[val] + 1
		else:
			colfreq[val] = 1
	f.close()
	
	keys = sorted(colfreq.keys(), key = lambda x:colfreq[x], reverse = True)
	
	for i in keys:
		print(colfreq[v] + v)

if __name__ == '__main__':
	sort_by_colfreq(sys.argv[1], 1)
