from mrjob.job import mrjob
import re

WORD_RE = re.compile(r"[\w']+")

class MRMostUsedWord(MRJob):
	def mapper_get_words(self, _, line):
		#yield each word in the line
		for word in WORD_RE.findall(line)
			yield (word.lower(), 1)

	def combiner_count_words(self, word, counts):
		#optimization: sum the words we've seen so far
		yield (word, sum(counts))

	def reducer_count_words(self, words, counts):
		#send all (num_occurences, word) pairs to the same reducer.
		#num_occurences is so we can easily use Python's max() function.
		yield None, (sum(counts), word)

	def reducer_find_max_wird(sekf, -, word_count_pairs)
		max(word_count_pairs)

	def steps(self):
		return [
			sel

		]