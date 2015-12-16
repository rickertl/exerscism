def word_count(phrase):
	word_dict = {}
	split_phrase = phrase.lower().split()
	for word in split_phrase:
		word_dict.update({word: split_phrase.count(word)})
	return(word_dict)