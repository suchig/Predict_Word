import spacy
from collections import defaultdict
from ngram_pred_util import nlp

class TextTokens:
	"""
	Class to create documents that provide tokens for a given text
	"""

	def __init__(self,text, matcher):
		"""
		Tokenizes the text based on 
		- Span list from named entities
		- Span list from manual list (get_matcher)
		Retains the tokens as instance variable
	
		Keyword arguments:
			text -- Corpus or text that has to be converted to tokens
			matcher - Matcher that provides patterns for manual span
		"""
		self.doc = nlp(text)
		spans = list(ent for ent in self.doc.ents if ent.label_ != 'WORK_OF_ART')

		spans_match = []
		matches = matcher(self.doc)
		spans_match = [self.doc[start:end] for _, start, end in matches]

		with self.doc.retokenize() as retokenizer:
			for span in spans:
				retokenizer.merge(span)

	def get_doc(self):
		"""
		returns the tokenized document
	
		Keyword arguments:
			--None--
		"""
		return self.doc

	def get_ngram_dict(self,num):
		"""
		Creates n_gram dictionary with 
		key being the n tokens 
		value being the next token 
	
		Keyword arguments:
			num -- integer representing n in n-gram
		"""
		ngrams_dict = defaultdict(list)
		for i in range(len(self.doc)-num):
			token=self.doc[i]
			pattern = ' '.join(token.text for token in self.doc[i:i+num])
			ngrams_dict[pattern].append(self.doc[i+num])
		return ngrams_dict