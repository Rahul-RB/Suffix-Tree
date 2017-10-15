def words_in_string(word_list, a_string):
	return set(word_list).intersection(a_string.split())

my_word_list = ['one', 'two', 'three']
a_string = 'one tw'

for word in words_in_string(my_word_list, a_string):
	print(word)
