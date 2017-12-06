"""
09. Typoglycemia

Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự space. Viết chương trình thực hiện việc sau:

    Với mỗi word, giữ nguyên ký tự đầu và ký tự cuối, đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của (tất nhiên các word có ít hơn 4 ký tự thì không cần làm gì)
    Cho trước một câu tiếng Anh hợp lệ, ví dụ "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .", chạy chương trình đã viết để đưa ra kết quả.
"""
import random

def shuffle_word(w):
	if len(w) < 4:
		return w
	neww = w[0]
	random_index = list(range(1, len(w) - 1))
	random.shuffle(random_index)
	
	for i in random_index:
		neww = neww + w[i]

	neww = neww + w[-1]
	return neww 

def typoglycemia(s):
	new_word = []
	temp_word = s.split()
	
	for i in temp_word:
		new_word.append(shuffle_word(i)) 
	return ' '.join(new_word)


if __name__ == '__main__':
	str_input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	print(typoglycemia(str_input))
