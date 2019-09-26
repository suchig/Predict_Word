import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')


def get_matcher():
	"""
	Reads additional elements to be taken as span (manual span)
	Creates a rule based pattern and adds them to matcher

    Keyword arguments:
    --None--
    """
	matcher = Matcher(nlp.vocab)

	try:
		with open("span_file.txt") as f:
			lines = f.readlines()
			for i, line in enumerate(lines):
				words = line.split()
				pattern = [{"LOWER": word} for word in words]
				matcher.add(str(i), None, pattern)
	except:
		pass
	
	return matcher

