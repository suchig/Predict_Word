# Predict Word

**Description:**
Predicts next word in given corpus using n-gram model

**Usage:**
python ngram_pred.py

**Assumptions:**
1. Minimum 3 tokens will be entered by the user as input
2. User will input the phrase verbatim from corpus
3. Logical end for output is determined when a period ('.') is encountered in corpus or if the token is a noun and pobj of the sentence. 
4. Output will be a list of items with each item ending with a noun (Example ["thwart Ultron 's plans of gaining access", "thwart Ultron 's plans of gaining access to nuclear missiles"])
5. Any manual concatenation of nouns (like user interface) is done through a text file span_file.txt
6. It is assumed that span_file.text will only hold tokens with simple pattern and no punctuation(example "user interface" and not "user's manual") 
7. ONLY Named entities that are Person, Organization and GPE are considered as Span
8. This methodology uses only 3-grams as keyword
9. JARVIS text has been cleaned manually for logical sentence structure. 
