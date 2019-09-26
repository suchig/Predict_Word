from TextTokens import *
from ngram_pred_util import *

if __name__ == "__main__":

	#Static text
	JARVIS_TEXT = "Just A Rather Very Intelligent System a.k.a JARVIS is created by Tony Stark. It's a natural-language and a sophisticated artificial intelligence user interface computer system, named after Edwin Jarvis, the butler who worked for Howard Stark. Though its primary duty is to automate Stark’s Malibu estate, the lifelike program fulfills many other needs for Stark, like being an information source for him, a diagnostic tool, a consultant and a voice of reason in Stark’s life. It was also responsible to provide security for Tony Stark's Mansion and Stark Tower. After creating the Mark II armor, Stark uploaded JARVIS into all of the Iron Man Armors, as well as allowing him to interact with the other Avengers, giving them valuable information during combat. JARVIS may be the one intellect Stark feels most comfortable opening up to. JARVIS can object to Stark’s commands if necessary. JARVIS speaks with a refined British accent, and is capable of back talk, sarcasm and condescension. During the Ultron Offensive, JARVIS was destroyed by Ultron, although his remaining programming codes unknowingly continued to thwart Ultron's plans of gaining access to nuclear missiles. His remains were found by Stark, who uploaded them into a synthetic body made of vibranium and, in conjunction with Ultron's personality and an Infinity Stone. JARVIS' duties were then taken over by FRIDAY."
	#Assume n-gram of 3
	NUM = 3

	#Get matcher for custom combination of nouns
	matcher = get_matcher()
	#Get tokens that is tokenized using Spacy
	main_corpus = TextTokens(JARVIS_TEXT,matcher)
	#Create a dictionary of 3-gram keys each associated with the next word
	ngrams_dict = main_corpus.get_ngram_dict(NUM)


	############# User Input ################## 
	print("+++++++++++++CORPUS++++++++++++++++++")
	print(JARVIS_TEXT)
	print("+++++++++++++++++++++++++++++++++++++")
	print("\n")

	#Continue until user enters DONE
	while True:
		user_input=input("Enter (min 3 words) phrase from corpus (Enter DONE to quit): ")

		#Break if user enters DONE
		if user_input == "DONE":
			break

		#Get tokens based on same principle as the main JARVIS corpus
		input_doc = TextTokens(user_input,matcher).get_doc()
		#If user entered less than 3 tokens ask them to re-enter
		if (len(input_doc)<3):
			print("Oops You need to enter more words")
			print("\n")
		else:
			#Take only the last 3 tokens as they are the ones that can provide next word
			input_token = [token.text for token in input_doc[-3:]]
			answer = []
			out = ""

			#Continue until a logical end is found
			while True:
				#Create a text sequence using the 3 tokens
				input_seq = " ".join(word for word in input_token)

				#If dictionary does not have the sequence as key, the user has not entered verbatim from corpus
				if input_seq not in ngrams_dict.keys():
					print("The phrase has to be verbatim from the corpus")
					print("\n")
					break

				#Get the token from dictionary value
				token = ngrams_dict[input_seq][0]
				
				#If token is ., the sentence has come to an end and hence output text is added to answer list
				# Logical end
				if token.text == '.':
					answer.append(out)
					break

				#Concatenate the text with output
				out = out+ token.text

				#If token is pobj then the object of the sentence is found which is a logical end.
				#This is applicable only if object is associated with a NOUN or PRONOUN
				#Logical end
				if (token.pos_ == "NOUN" or token.pos_ == "PROPN") and token.dep_=="pobj":
					out = out.strip()
					answer.append(out)
					break

				#If logical end is not reached but we encounter a Noun, 
				#it is a logical place to add the incremental output to a list
				if token.tag_ == "NN":
					answer.append(out)

				#Remove the first token of the 3 word ngram 
				input_token.pop(0)

				#Add the next word (new token's text) as the next token
				input_token.append(token.text)
				out = out+" "
			#Print the answer list
			print(answer)
			print("\n")
