def vowel_checker(word):
	word = word.lower()
	count = 0
	for i in word:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			count+=1

	return count