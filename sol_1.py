""" 01. Trích xuất ký tự từ xâu ký tự
Từ xâu ký tự "MPyaktQrBoilk RCSahr", hãy trích xuất các ký tự ở vị trí 2,4,6,8,10,12,14,16,18,20 và kết hợp theo thứ tự đó để tạo thành 1 xâu ký tự mới (ký tự space cũng được tính, các ký tự được đánh số từ 1).
"""

def extract():
	temp = "MPyaktQrBoilk RCSahr"
	new_str = temp[1:21:2]
	print(new_str)

if __name__ == '__main__':
	extract()
	
