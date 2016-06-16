def get_word():
	mas = []
	while True:
		text = input()
		if text == '':
			break
		else:
			text = text.split(' ')
			for t in text:
				mas.append(t)
	count = {}

	for word in mas:
		count[word] = count[word]+1 if word in count else 1
	count = sorted(count.items(), key = lambda x: x[1], reverse=True)
	return '---' if len(count) > 1 and count[0][1] == count[1][1] else count[0][0]

print(get_word())