
def match(phrase):
	phrases = [
    "what time is it",
    "what's the weather",
    "what's the date",
    "hello",
    "hi",
    "what's up",
    "how are you"
]

	match_word_dict = {}
	for element in phrases:
		sameness = 0
		for index in range(len(element)):
			if len(phrase) == index:
				break
			if phrase[index] == element[index]:
				sameness += 1
			
		

		percent = (sameness * 1.0 / len(element) * 1.0) * 100
		match_word_dict[element] = percent
	return match_word_dict

print match("halao")
