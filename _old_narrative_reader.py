import nltk
import docx2txt

filename= "GC.docx"
text = docx2txt.process(filename)

def unusual_words(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

token_list = nltk.word_tokenize(text)

stopwords_removed = [word for word in token_list if word not in stopwords.words('english')]

def filter_duplicates(text_list):
	output_list = []
	for word in text_list:
		if word not in output_list:
			output_list.append(word)
	return output_list


from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
stemmed = []
for word in filtered:
		stemmed.append(st.stem(word))

"""

create client corpus list
 {"gocardless" : [u'techn', u'nar', u'lead', u'rol'... u'gocardless'],
  "geckoboard" : [u'dash', u'api', u'data' ... u'geckoboard']}

create grant corpus list
	{"smart": ["etc"]}
"""

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems
