"""
16. Chia file thành N phần

Chia file thành các files nhỏ với N lines mỗi file (đơn vị là các hàng trong file). Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N. Sử dụng lệnh split để thực hiện công việc (split -l N).

Sau đó, cải tiến chương trình để chia file thành thành N phần bằng nhau (thay vì N lines mỗi file).
"""
import sys
import string

def writelines(filename, lines):
	f = open(filename, 'w')
	f.writelines(lines)
	f.close()

#return the next filename given the current filename
def next_filename(current):
	suffix_len = len(current) - 1
	alphabets = list(string.ascii_lowercase)
	charidx = {}
	
	for i in range(len(alphabets)):
		charidx[alphabets[i]] = i

	if suffix_len == 0:
		return None

	last_char_idx = charidx[current[suffix_len]]

	if last_char_idx < len(alphabets) - 1:
		return current[0:suffix_len] + alphabets[last_char_idx + 1]
	else:
		prefx = next_filename(current[0:suffix_len])
		if prefix == None:
			return None
		else:
			return prefix + 'a'

def split_by_nlines(filename, nlines, suffix_length = 2):
	f = open(filename, 'rU')
	lines = f.readlines()
	f.close()

	nfile = int(len(lines) / nlines)
	if nfile * nlines < len(lines):
		nfile = nfile + 1

	prefix = 'x'
	current = prefix + 'a' * suffix_length
	for i in range(nfile):
		filename = current
		l = i * nlines
		r = min( (i + 1) * nlines, len(lines))
		writelines(filename, lines[l:r])
		current = next_filename(current)

def split_by_nfiles(filename, nfiles, suffix_length = 2):
	f = open(filename, 'rU')
	lines = f.readlines()
	f.close()

	prefix = 'x'
	currentf = prefix + 'a' * suffix_length
	nlines = int(len(lines) / nfiles)

	resi = len(lines) - nlines * nfiles

	l = 0
	r = 0
	for i in range(nfiles - resi):
		filename = currentf
		l = r
		r = l + nlines
		writelines(filename, lines[l:r])
		currentf = next_filename(currentf)

	for i in range(nfiles - resi, nfiles):
		filename = currentf
		l = r
		r = l + (nlines + 1)
		writelines(current, lines[l:r])
		currentf = next_filename(currentf)


if __name__ == '__main__':
	args = sys.argv[1:]

	check_split_file = False
	if args[0] == '--files':
		check_split_file = True
		del args[0]

	n = int(args[0])
	filename = "./../HSHG.txt"
	if check_split_file:
		split_by_nfiles(filename, n)
	else:
		split_by_nlines(filename, n)

