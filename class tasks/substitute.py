def reversed_string(name):
	reversed_word = ''
	for number in range(len(name)-1,-1, -1):
		reversed_word += name[number]

	return reversed_word
print(reversed_string("mummy wa"))
